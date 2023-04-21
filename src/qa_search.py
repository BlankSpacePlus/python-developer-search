from datetime import datetime
from flask import Flask, render_template, jsonify, request

import json
import os
import re
import time

from whoosh import index
from whoosh import qparser
from whoosh.analysis import *
from whoosh.fields import *
from whoosh.index import create_in, exists_in, open_dir
from whoosh.qparser.dateparse import DateParserPlugin
from whoosh.qparser.plugins import GtLtPlugin
from wsgiref.simple_server import make_server


app = Flask(__name__)


@app.route('/')
def index():
        # 默认界面
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    t = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
    print('ip:', ip, 't:', t)
    with open("../log/qa_search.log", "a", encoding="UTF-8") as f:
        # 追加写模式
        f.write(f"{ip} {t}\n")
    return render_template('index.html')


@app.route('/search/<query>', methods=['POST', 'GET'])
def search(query):
    begin_time = time.time()
    print(query)
    results, result_count = get_qa_top_k(query)
    end_time = time.time()
    run_time = round(end_time - begin_time, 2)
    run_time = str(run_time)
    new_results = []
    for result in results:
        new_results.append({'data_type': 'qa', 'result_data': result})
    return jsonify({"result": new_results, 'run_time': run_time, 'result_num': result_count})


def logging_setting():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    t = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
    print('ip:', ip, 't:', t)
    with open("../log/qa_search.log", "a", encoding="UTF-8") as f:
        # 追加写模式
        f.write(f"{ip} {t}\n")


def init_index():
    # Schema用法详见 https://whoosh.readthedocs.io/en/latest/schema.html
    schema = Schema(re_query=TEXT(stored=False, analyzer=StemmingAnalyzer()), qc=STORED())
    files = ["query_code_json"]
    query_code_list = list()
    for file_name in files:
        with open(f"../data/{file_name}.json", 'r', encoding="UTF-8") as f:
            data = json.load(f)
        query_code_list.extend(data)
    index_dir = '../data/index/'
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    if exists_in(index_dir):
        # 直接读入已有的索引
        data_index = open_dir(index_dir)
    else:
        data_index = create_in(index_dir, schema)
        print("building index ...")
        writer = data_index.writer()
        for s in query_code_list:
            re_query = s["re_query"]
            qc = s["qc"]
            writer.add_document(re_query=re_query, qc=qc)
        writer.commit()
        print("end of building index ...")
    field_name = "re_query"  # 默认的field
    og = qparser.OrGroup.factory(0.9)  # factory是or的情况下，偏向于同时满足多个条件
    parser = qparser.QueryParser(field_name, schema=schema, group=og)  # 这里都是default
    parser.add_plugin(DateParserPlugin())
    parser.add_plugin(GtLtPlugin())  # 可以使用>,<等
    parser.add_plugin(qparser.FuzzyTermPlugin())  # 支持模糊查询 cat~2
    global INDEX, PARSER
    INDEX = data_index
    PARSER = parser


def get_qa_top_k(query: str, k: int = 10):
    init_index()
    results = list()
    global INDEX, PARSER
    q = PARSER.parse(query)
    with INDEX.searcher() as s:
        results = s.search(q, limit=10)
        # 必须要放在里面，searcher关闭之后就不能读了
        results_count = len(results)
        if results_count != 0:
            results = [_["qc"] for _ in results[:k]]  # 取前5个结果
        print(results)
    return results, results_count


INDEX = None
PARSER = None


if __name__ == '__main__':
    init_index()
    app.run(host='0.0.0.0', debug=True)

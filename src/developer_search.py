import code_search
from datetime import datetime
from flask import Flask, render_template, jsonify, request
import json
import logging
import os
import qa_search
import re
import time
import torch
import transformers
from transformers import AutoTokenizer, AutoModel


app = Flask(__name__)

# model = AutoModel.from_pretrained('../model/code_search/checkpoint-best')
# tokenizer = AutoTokenizer.from_pretrained('../model/codebert')
# index = load_index('path/to/your/index')
# query = 'your query code snippet'
# encoded_query = tokenizer.encode(query, return_tensors='pt')
# with torch.no_grad():
#     query_vector = model(encoded_query)[0][0]
#     results = index.search(query_vector, k=num_results)

@app.route('/')
def index():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    app.logger.info(f"access from ip:{ip}")
    return render_template('index.html')


@app.route('/search/<query>', methods=['POST', 'GET'])
def search(query):
    begin_time = time.time()
    print(query)
    qa_results, qa_results_count = qa_search.get_qa_top_k(query, 10)
    print(qa_results)
    code_results, code_results_count = code_search.get_code_top_k(query, 10)
    print(code_results)
    results_count = qa_results_count + code_results_count
    new_results = []
    for result in qa_results:
        new_results.append({'data_type': 'qa', 'result_data': result})
        app.logger.info(result)
    for result in code_results:
        new_results.append({'data_type': 'code', 'result_data': result})
        app.logger.info(result)
    # print(new_results)
    end_time = time.time()
    run_time = round(end_time - begin_time, 2)
    run_time = str(run_time)
    return jsonify({"result": new_results, 'run_time': run_time, 'result_num': results_count})


def logging_setting():
    handler1 = logging.FileHandler(filename="../log/developer_search.log", encoding="utf-8")
    app.logger.setLevel(logging.DEBUG)
    handler1.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s")
    handler1.setFormatter(formatter)
    app.logger.addHandler(handler1)


if __name__ == '__main__':
    logging_setting()
    qa_search.init_index()
    app.run(host='0.0.0.0', debug=True)

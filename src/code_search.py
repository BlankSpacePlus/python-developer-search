from flask import Flask, render_template, jsonify, request
import code_matcher_utils
import code_search_parse
from code_search_index import SearchEngine
import code_search_rerank
import logging
from flask_cors import CORS

se = SearchEngine()
app = Flask(__name__)
jdk = code_matcher_utils.load_pkl('../data/jdk_vocab.pkl')
CORS(app, supports_credentials=True)


@app.route('/')
def index():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    app.logger.info(f"access from ip:{ip}")
    return render_template('index.html')


@app.route('/search/<query>', methods=['POST', 'GET'])
def search(query):
    app.logger.info("query" + "*" * 50)
    app.logger.info(query)
    results = get_code_top_k(query, k=10)
    app.logger.info("results" + "*" * 50)
    new_results = []
    for result in results:
        new_results.append({'data_type': 'code', 'result_data': result})
        app.logger.info(result)
    json = jsonify({"result": new_results})
    return json


def get_code_top_k(query: str, k: int = 10):
    query_parse = code_search_parse.parse(query)
    data, cmds = se.fuzzy_search(query_parse, top_k=10)
    results = code_search_rerank.reranking(query_parse, data, cmds, jdk)
    results_count = len(results)
    print(results)
    return results, results_count


def logging_setting():
    handler1 = logging.FileHandler(filename="../log/code_search.log", encoding="utf-8")
    # handler2 = logging.StreamHandler()
    app.logger.setLevel(logging.DEBUG)
    handler1.setLevel(logging.INFO)
    # handler2.setLevel(logging.NOTSET)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s")
    handler1.setFormatter(formatter)
    # handler2.setFormatter(formatter)
    app.logger.addHandler(handler1)
    # app.logger.addHandler(handler2)


if __name__ == '__main__':
    # setting debug as True if you want to see details
    # app.debug = True
    logging_setting()
    app.run(host='0.0.0.0')

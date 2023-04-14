import json
from query_rewriter_model import QueryRewriter
import re


cnt = 1
query_code_list = []
query_rewriter_model = QueryRewriter()

# https://drive.google.com/file/d/1w8GKMmVVYufIr0F0JlxL7T9d880K-2mc/view?usp=share_link
for line in open("../data/java-code-selection.train"):
    line_elements = re.split(r'\t', line)
    query = line_elements[1]
    code_snippet = line_elements[3]
    query_vector = query_rewriter_model.encode(query)
    query_paraphrase = query_rewriter_model.paraphrase(query)
    # 非空
    if query_paraphrase:
        query_code_map = {'query': query, 'code': code_snippet}
        data_map = {'id': cnt, 're_query': query_paraphrase[0], 'qc': query_code_map}
        query_code_list.append(data_map)
        print(cnt)
    cnt += 1

query_code_json = json.dumps(query_code_list, ensure_ascii=False)
json_file = open('../data/query_code_json.json', 'w')
json_file.write(query_code_json)
json_file.close()

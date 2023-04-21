import json
from query_rewriter_model import QueryRewriter
import re

cnt = 1
question_answer_list = []
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
        question_answer_map = {'question': query, 'answer': code_snippet}
        data_map = {'id': cnt, 're_question': query_paraphrase[0], 'qa': question_answer_map}
        question_answer_list.append(data_map)
        print(cnt)
    cnt += 1

question_answer_json = json.dumps(question_answer_list, ensure_ascii=False)
json_file = open('../data/question_code_json.json', 'w')
json_file.write(question_answer_json)
json_file.close()

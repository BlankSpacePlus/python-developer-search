import torch
import transformers
from transformers import AutoTokenizer, AutoModel
from qa_search import get_qa_top_k

# model = AutoModel.from_pretrained('../model/code_search/checkpoint-best')
# tokenizer = AutoTokenizer.from_pretrained('../model/codebert')
# index = load_index('path/to/your/index')
# query = 'your query code snippet'
# encoded_query = tokenizer.encode(query, return_tensors='pt')
# with torch.no_grad():
#     query_vector = model(encoded_query)[0][0]
#     results = index.search(query_vector, k=num_results)

print(get_qa_top_k("How to use ArrayList?", 10))

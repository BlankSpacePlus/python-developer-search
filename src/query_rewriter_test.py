from query_rewriter_model import QueryRewriter

query = "How do I use Java to read from a file that is actively being written to?"

# Initialize the model
QR_model = QueryRewriter()
# Get the embedding of a query
query_vec = QR_model.encode(query)

# Get the paraphrase questions of a query
paraphrase_q = QR_model.paraphrase(query)
print(paraphrase_q)

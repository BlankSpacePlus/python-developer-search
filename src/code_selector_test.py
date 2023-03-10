from code_selector_model import CodeSelector

query = "how do i compare strings in java?"
code_snippet = "a.compareTo(b)"
code_snippets = ["a.compareTo(b)", "String a = \"123\"; a.compareTo(b);"]

# Initialize the CodeSelector Model
cs_model = CodeSelector()

# Estimate the matching score between a query and a code snippet
score = cs_model.get_score(query, code_snippet)
print(score)
scores = cs_model.get_candidate_scores(query, code_snippets)
print(scores)

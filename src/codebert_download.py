from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")
tokenizer.save_pretrained('../model/codebert/')  # Model
model.save_pretrained('../model/codebert/')  # Model

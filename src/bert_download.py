from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")
tokenizer.save_pretrained('../model/bert/')  # Model
model.save_pretrained('../model/bert/')  # Model

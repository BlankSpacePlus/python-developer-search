import numpy as np
import pickle
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from transformers import T5Tokenizer, T5Model


def set_seed(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


set_seed(42)


class QueryRewriter(object):

    def __init__(self):
        self.device = self.get_device()
        self.model = self.load_model()
        self.tokenizer = self.load_tokenizer()
        self.input_embeddings = self.load_input_embeddings()
        print(type(self.input_embeddings))
        pass

    def get_device(self):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        return device

    def load_model(self):
        model = T5ForConditionalGeneration.from_pretrained('../model/t5_paraphrase')
        model = model.to(self.device)
        return model

    def load_tokenizer(self):
        tokenizer = T5Tokenizer.from_pretrained('../model/t5_paraphrase')
        return tokenizer

    def load_input_embeddings(self):
        embeddings = self.model.get_input_embeddings()
        return embeddings

    def encode(self, query):
        query = query.strip()
        text = query
        input_ids = self.tokenizer.encode(text, return_tensors="pt").to(self.device)
        ################ Alternative Method ############################
        outputs = self.input_embeddings(input_ids)
        outputs = torch.squeeze(outputs)
        output_vec = outputs.cpu().detach().numpy()
        output_vec = np.mean(output_vec, axis=0)
        return output_vec

    def paraphrase(self, query):
        query = query.strip()
        text = "paraphrase: " + query + " </s>"
        max_len = 256
        encoding = self.tokenizer.encode_plus(text, pad_to_max_length=True, return_tensors="pt")
        input_ids, attention_masks = encoding["input_ids"].to(self.device), encoding["attention_mask"].to(self.device)
        beam_outputs = self.model.generate(
            input_ids=input_ids,
            attention_mask=attention_masks,
            do_sample=True,
            max_length=256,
            top_k=120,
            top_p=0.95,
            early_stopping=True,
            num_return_sequences=3
        )
        final_outputs = []
        for beam_output in beam_outputs:
            sent = self.tokenizer.decode(beam_output, skip_special_tokens=True, clean_up_tokenization_spaces=True)
            if sent.lower() != query.lower() and sent not in final_outputs:
                final_outputs.append(sent)
        return final_outputs

from code_selector_utils import *
from bert_mlp import Model, Config


class CodeSelector(object):

    def __init__(self):
        self.config = Config()
        self.model = self.load_model()
        self.tokenizer = self.load_tokenizer()
        pass

    def load_model(self):
        PATH = '../model/code_selector/model.ckpt'
        model = Model(self.config).to(self.config.device)
        model.load_state_dict(torch.load(PATH))
        model.eval()
        print('Model Loaded!')
        return model

    def load_tokenizer(self):
        tokenizer = AutoTokenizer.from_pretrained('../model/bert')
        print("Tokenizer Loaded!")
        return tokenizer
        pass

    def encode_qc(self, question, cs):
        encoded_qc = self.tokenizer(question, cs, padding=True, truncation=True, max_length=128, return_tensors='pt')
        return encoded_qc

    def get_score(self, question, cs):
        # encode qc_0
        encoded_qc0 = self.encode_qc(question, cs)
        qc0_input_ids = encoded_qc0['input_ids']
        qc0_token_type_ids = encoded_qc0['token_type_ids']
        qc0_attention_masks = encoded_qc0['attention_mask']
        # encode qc_1 
        encoded_qc1 = self.encode_qc('', '')
        qc1_input_ids = encoded_qc1['input_ids']
        qc1_token_type_ids = encoded_qc1['token_type_ids']
        qc1_attention_masks = encoded_qc1['attention_mask']
        # to device 
        b_qc0_input_ids = qc0_input_ids.to(self.config.device)
        b_qc0_input_mask = qc0_attention_masks.to(self.config.device)
        b_qc0_input_types = qc0_token_type_ids.to(self.config.device)
        b_qc1_input_ids = qc1_input_ids.to(self.config.device)
        b_qc1_input_mask = qc1_attention_masks.to(self.config.device)
        b_qc1_input_types = qc1_token_type_ids.to(self.config.device)
        with torch.no_grad():
            qc0 = (b_qc0_input_ids, b_qc0_input_mask, b_qc0_input_types)
            qc1 = (b_qc1_input_ids, b_qc1_input_mask, b_qc1_input_types)
            outputs = self.model(qc0, qc1)
        score = outputs.data.cpu().numpy()[0][1]
        return score

    def get_candidate_scores(self, question, candidate_answers):
        candidate_scores = []
        for cs in candidate_answers:
            score = self.get_score(question, cs)
            candidate_scores.append(score)
        return candidate_scores


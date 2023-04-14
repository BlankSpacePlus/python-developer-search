# StackOverflow开发者搜索

![](./images/stack-overflow.png)

## 数据获取

- CodeSearchNet
    - [CodeSearchNet Challenge: Evaluating the State of Semantic Code Search](https://arxiv.org/abs/1909.09436)
    - [GitHub Repository](https://github.com/github/CodeSearchNet)
- StackExchange
    - [StackExchange](https://stackexchange.com)
    - [StackOverflow](https://stackoverflow.com)
    - 数据示例：
        ```javascript
        {
            "id": 1,
            "re_query": "how to make the division of 2 ints produce a float instead of another int?",
            "qc": {
                "query": "How can I increment a variable without exceeding a maximum value?",
                "code": "health = health < NUM ? health + NUM : NUM ;"
            }
      },
        ```

## 模型选择

- BERT
    - [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://aclanthology.org/N19-1423/)
    - [GitHub Repository](https://github.com/google-research/bert)
- T5
    - [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://jmlr.org/papers/v21/20-074.html)
    - [GitHub Repository](https://github.com/google-research/text-to-text-transfer-transformer)
- Que2Code
    - [I Know What You Are Searching For: Code Snippet Recommendation from Stack Overflow Posts](https://arxiv.org/abs/2210.15845)
    - [GitHub Repository](https://github.com/beyondacm/Que2Code)
        - [CodeSelector](https://github.com/beyondacm/Que2Code/tree/main/CodeSelector)
        - [QueryRewriter](https://github.com/beyondacm/Que2Code/tree/main/QueryRewriter)
- CodeBERT
    - [CodeBERT: A Pre-Trained Model for Programming and Natural Languages](https://aclanthology.org/2020.findings-emnlp.139)
    - [GitHub Repository](https://github.com/microsoft/CodeBERT)

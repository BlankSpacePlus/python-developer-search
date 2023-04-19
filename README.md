# StackOverflow开发者搜索

![](./images/stack-overflow.png)

## 工程结构

├── data<br>
│   ├── codesearch<br>
│   │   ├── java_test_0.jsonl.gz<br>
│   │   ├── test<br>
│   │   │   └── java<br>
│   │   │       ├── batch_0.txt<br>
│   │   │       ├── batch_10.txt<br>
│   │   │       ├── batch_11.txt<br>
│   │   │       ├── batch_121.txt<br>
│   │   │       ├── batch_12.txt<br>
│   │   │       ├── batch_13.txt<br>
│   │   │       ├── batch_14.txt<br>
│   │   │       ├── batch_15.txt<br>
│   │   │       ├── batch_16.txt<br>
│   │   │       ├── batch_17.txt<br>
│   │   │       ├── batch_18.txt<br>
│   │   │       ├── batch_19.txt<br>
│   │   │       ├── batch_1.txt<br>
│   │   │       ├── batch_20.txt<br>
│   │   │       ├── batch_21.txt<br>
│   │   │       ├── batch_22.txt<br>
│   │   │       ├── batch_23.txt<br>
│   │   │       ├── batch_24.txt<br>
│   │   │       ├── batch_25.txt<br>
│   │   │       ├── batch_2.txt<br>
│   │   │       ├── batch_3.txt<br>
│   │   │       ├── batch_4.txt<br>
│   │   │       ├── batch_5.txt<br>
│   │   │       ├── batch_6.txt<br>
│   │   │       ├── batch_7.txt<br>
│   │   │       ├── batch_8.txt<br>
│   │   │       ├── batch_9.txt<br>
│   │   │       └── cached_test_batch_121_codebert_200_codesearch<br>
│   │   ├── train.log<br>
│   │   └── train_valid<br>
│   │       └── java<br>
│   │           ├── cached_dev_valid_codebert_200_codesearch<br>
│   │           ├── cached_train_train_codebert_200_codesearch<br>
│   │           ├── train.txt<br>
│   │           └── valid.txt<br>
│   ├── code-snippet.txt<br>
│   ├── index<br>
│   │   ├── _MAIN_1.toc<br>
│   │   ├── MAIN_dhb9stsudccfjdhy.seg<br>
│   │   └── MAIN_WRITELOCK<br>
│   ├── java-code-selection.train<br>
│   ├── query_code_json.json<br>
│   └── query.txt<br>
├── images<br>
│   └── stack-overflow.png<br>
├── LICENSE<br>
├── log<br>
│   └── main.log<br>
├── model<br>
│   ├── bert<br>
│   │   ├── config.json<br>
│   │   ├── pytorch_model.bin<br>
│   │   ├── special_tokens_map.json<br>
│   │   ├── tokenizer_config.json<br>
│   │   ├── tokenizer.json<br>
│   │   └── vocab.txt<br>
│   ├── codebert<br>
│   │   ├── config.json<br>
│   │   ├── merges.txt<br>
│   │   ├── pytorch_model.bin<br>
│   │   ├── special_tokens_map.json<br>
│   │   ├── tokenizer_config.json<br>
│   │   └── vocab.json<br>
│   ├── code_search<br>
│   │   ├── checkpoint-best<br>
│   │   │   ├── config.json<br>
│   │   │   ├── optimizer.pt<br>
│   │   │   ├── pytorch_model.bin<br>
│   │   │   ├── scheduler.pt<br>
│   │   │   ├── training_0.bin<br>
│   │   │   ├── training_1.bin<br>
│   │   │   └── training_2.bin<br>
│   │   ├── checkpoint-last<br>
│   │   │   ├── config.json<br>
│   │   │   ├── idx_file.txt<br>
│   │   │   ├── optimizer.pt<br>
│   │   │   ├── pytorch_model.bin<br>
│   │   │   ├── scheduler.pt<br>
│   │   │   └── step_file.txt<br>
│   │   ├── config.json<br>
│   │   ├── eval_results.txt<br>
│   │   ├── merges.txt<br>
│   │   ├── pytorch_model.bin<br>
│   │   ├── special_tokens_map.json<br>
│   │   ├── tokenizer_config.json<br>
│   │   ├── training_args.bin<br>
│   │   └── vocab.json<br>
│   ├── code_selector<br>
│   │   ├── config.json<br>
│   │   ├── model.ckpt<br>
│   │   ├── pytorch_model.bin<br>
│   │   ├── tokenizer_config.json<br>
│   │   ├── tokenizer.json<br>
│   │   └── training_stats.json<br>
│   └── t5_paraphrase<br>
│       ├── config.json<br>
│       ├── pytorch_model.bin<br>
│       ├── special_tokens_map.json<br>
│       ├── spiece.model<br>
│       └── tokenizer_config.json<br>
├── README.md<br>
├── requirements.txt<br>
├── result<br>
│   └── code_search<br>
│       └── 121_batch_result.txt<br>
└── src<br>
    ├── bert_mlp.py<br>
    ├── check_code_selection_data.py<br>
    ├── codebert_fine_tune.sh<br>
    ├── codebert_inference.sh<br>
    ├── codebert_process_data.py<br>
    ├── codebert_run_classifier.py<br>
    ├── codebert_utils.py<br>
    ├── code_selector_model.py<br>
    ├── code_selector_process_data.py<br>
    ├── code_selector_test.py<br>
    ├── code_selector_utils.py<br>
    ├── download_bert.py<br>
    ├── download_codebert.py<br>
    ├── models<br>
    │   └── java<br>
    ├── \_\_pycache\_\_<br>
    │   ├── bert_mlp.cpython-37.pyc<br>
    │   ├── codebert_utils_2.cpython-38.pyc<br>
    │   ├── codebert_utils.cpython-38.pyc<br>
    │   ├── code_selector_model.cpython-37.pyc<br>
    │   ├── code_selector_utils.cpython-37.pyc<br>
    │   ├── flask_show.cpython-37.pyc<br>
    │   ├── parsing.cpython-37.pyc<br>
    │   ├── query_rewriter_model.cpython-37.pyc<br>
    │   └── util.cpython-37.pyc<br>
    ├── qa_search.py<br>
    ├── query_code_pair_search.py<br>
    ├── query_rewriter_model.py<br>
    ├── query_rewriter_test.py<br>
    ├── runs<br>
    ├── static<br>
    │   ├── css<br>
    │   │   ├── a11y-light.css<br>
    │   │   ├── codestyle.css<br>
    │   │   ├── index.css<br>
    │   │   ├── like.css<br>
    │   │   ├── load.css<br>
    │   │   ├── style.css<br>
    │   │   └── waitMe.css<br>
    │   ├── img<br>
    │   │   ├── dislike.gif<br>
    │   │   ├── favicon.ico<br>
    │   │   ├── like.gif<br>
    │   │   └── search-white.png<br>
    │   ├── js<br>
    │   │   ├── highlight.pack.js<br>
    │   │   ├── index.js<br>
    │   │   ├── jquery-1.11.0.min.js<br>
    │   │   ├── jquery.codestyle.js<br>
    │   │   ├── jquery.codestyle.min.js<br>
    │   │   ├── like.js<br>
    │   │   └── wait.js<br>
    │   └── lib<br>
    │       ├── bootstrap-4.1.3-dist<br>
    │       │   ├── css<br>
    │       │   │   ├── bootstrap.css<br>
    │       │   │   ├── bootstrap.css.map<br>
    │       │   │   ├── bootstrap-grid.css<br>
    │       │   │   ├── bootstrap-grid.css.map<br>
    │       │   │   ├── bootstrap-grid.min.css<br>
    │       │   │   ├── bootstrap-grid.min.css.map<br>
    │       │   │   ├── bootstrap.min.css<br>
    │       │   │   ├── bootstrap.min.css.map<br>
    │       │   │   ├── bootstrap-reboot.css<br>
    │       │   │   ├── bootstrap-reboot.css.map<br>
    │       │   │   ├── bootstrap-reboot.min.css<br>
    │       │   │   └── bootstrap-reboot.min.css.map<br>
    │       │   └── js<br>
    │       │       ├── bootstrap.bundle.js<br>
    │       │       ├── bootstrap.bundle.js.map<br>
    │       │       ├── bootstrap.bundle.min.js<br>
    │       │       ├── bootstrap.bundle.min.js.map<br>
    │       │       ├── bootstrap.js<br>
    │       │       ├── bootstrap.js.map<br>
    │       │       ├── bootstrap.min.js<br>
    │       │       └── bootstrap.min.js.map<br>
    │       └── jquery-3.3.1.min.js<br>
    ├── templates<br>
    │   └── index.html<br>
    └── torch_cuda_test.py<br>

## 数据获取

- CodeSearchNet
    - [CodeSearchNet Challenge: Evaluating the State of Semantic Code Search](https://arxiv.org/abs/1909.09436)
    - [GitHub Repository](https://github.com/github/CodeSearchNet)
    - 数据示例：
        ```javascript
        {
            "repo": "googleapis/google-cloud-java",
            "path": "google-cloud-clients/google-cloud-pubsub/src/main/java/com/google/cloud/pubsub/v1/SubscriptionAdminClient.java",
            "func_name": "SubscriptionAdminClient.modifyPushConfig",
            "original_string": "public final void modifyPushConfig(String subscription, PushConfig pushConfig) {\n\n    ModifyPushConfigRequest request =\n        ModifyPushConfigRequest.newBuilder()\n            .setSubscription(subscription)\n            .setPushConfig(pushConfig)\n            .build();\n    modifyPushConfig(request);\n  }",
            "language": "java",
            "code": "public final void modifyPushConfig(String subscription, PushConfig pushConfig) {\n\n    ModifyPushConfigRequest request =\n        ModifyPushConfigRequest.newBuilder()\n            .setSubscription(subscription)\n            .setPushConfig(pushConfig)\n            .build();\n    modifyPushConfig(request);\n  }",
            "code_tokens": ["public", "final", "void", "modifyPushConfig", "(", "String", "subscription", ",", "PushConfig", "pushConfig", ")", "{", "ModifyPushConfigRequest", "request", "=", "ModifyPushConfigRequest", ".", "newBuilder", "(", ")", ".", "setSubscription", "(", "subscription", ")", ".", "setPushConfig", "(", "pushConfig", ")", ".", "build", "(", ")", ";", "modifyPushConfig", "(", "request", ")", ";", "}"],
            "docstring": "Modifies the `PushConfig` for a specified subscription.\n\n<p>This may be used to change a push subscription to a pull one (signified by an empty\n`PushConfig`) or vice versa, or change the endpoint URL and other attributes of a push\nsubscription. Messages will accumulate for delivery continuously through the call regardless of\nchanges to the `PushConfig`.\n\n<p>Sample code:\n\n<pre><code>\ntry (SubscriptionAdminClient subscriptionAdminClient = SubscriptionAdminClient.create()) {\nProjectSubscriptionName subscription = ProjectSubscriptionName.of(\"[PROJECT]\", \"[SUBSCRIPTION]\");\nPushConfig pushConfig = PushConfig.newBuilder().build();\nsubscriptionAdminClient.modifyPushConfig(subscription.toString(), pushConfig);\n}\n</code></pre>\n\n@param subscription The name of the subscription. Format is\n`projects/{project}/subscriptions/{sub}`.\n@param pushConfig The push configuration for future deliveries.\n<p>An empty `pushConfig` indicates that the Pub/Sub system should stop pushing messages\nfrom the given subscription and allow messages to be pulled and acknowledged - effectively\npausing the subscription if `Pull` or `StreamingPull` is not called.\n@throws com.google.api.gax.rpc.ApiException if the remote call fails",
            "docstring_tokens": ["Modifies", "the", "PushConfig", "for", "a", "specified", "subscription", "."],
            "sha": "d2f0bc64a53049040fe9c9d338b12fab3dd1ad6a",
            "url": "https://github.com/googleapis/google-cloud-java/blob/d2f0bc64a53049040fe9c9d338b12fab3dd1ad6a/google-cloud-clients/google-cloud-pubsub/src/main/java/com/google/cloud/pubsub/v1/SubscriptionAdminClient.java#L1291-L1299",
            "partition": "train"
        }
        ```
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

lang=java #programming language
idx=121 #test batch idx

python codebert_run_classifier.py \
--model_type roberta \
--model_name_or_path ../model/codebert \
--task_name codesearch \
--do_predict \
--output_dir ./models/$lang \
--data_dir ../data/codesearch/test/$lang \
--max_seq_length 200 \
--per_gpu_train_batch_size 32 \
--per_gpu_eval_batch_size 32 \
--learning_rate 1e-5 \
--num_train_epochs 8 \
--test_file batch_${idx}.txt \
--pred_model_dir ../model/code_search/checkpoint-best/ \
--test_result_dir ../result/code_search/${idx}_batch_result.txt

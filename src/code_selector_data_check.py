for line in open("../../Que2Code-DataSet/java-code-selection/code-selection.train"):
    if "reading a plain text file in java" in line:
        print(1)
        print(line)
        break
for line in open("../../Que2Code-DataSet/java-code-selection/code-selection.val"):
    if "reading a plain text file in java" in line:
        print(2)
        print(line)
        break
for line in open("../../Que2Code-DataSet/java-code-selection/all_label_data.txt"):
    if "reading a plain text file in java" in line:
        print(3)
        print(line)
        break
for line in open("../../Que2Code-DataSet/java-duplicate-question/duplicate_questions.train"):
    if "reading a plain text file in java" in line:
        print(4)
        print(line)
        break
for line in open("../../Que2Code-DataSet/java-duplicate-question/duplicate_questions.test"):
    if "reading a plain text file in java" in line:
        print(5)
        print(line)
        break
for line in open("../../Que2Code-DataSet/java-duplicate-question/duplicate_questions.val"):
    if "reading a plain text file in java" in line:
        print(6)
        print(line)
        break

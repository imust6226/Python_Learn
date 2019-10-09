#coding = utf-8

file_path1 = 'alice.txt'
file_path2 = 'C:\Desktop\Admin\alice.txt'

try:
    with open(file_path2) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("Sorry,The File's Not Found!")
except Exception:
    print("Unknown Error")
else:
    print(contents)


# 使用 split()方法，可以通过空格来截取内容
words = "Alice in Wonderland"

word_list = words.split()
print(word_list)


# 计算文件中的单词数量
try:
    with open(file_path1) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("Sorry,The File's Not Found!")
except Exception:
    print("Unknown Error")
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + file_path1 + " has about " + str(num_words) + " words")

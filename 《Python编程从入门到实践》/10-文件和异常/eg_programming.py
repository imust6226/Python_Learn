#coding = utf-8

file_path = 'programming.txt'

print("写入空文件")

with open(file_path, 'w') as file_object:
    file_object.write("I love Programming.")
    # 写入多行文件，不会换行直接添加在末尾，需要使用\n来人工换行
    file_object.write("I love a new game.\n")
    file_object.write("I love this.")


print("追加内容到文件中去\n")

with open(file_path, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets,\n")
    file_object.write("I love creating apps that can run in a browser.\n")


#coding = utf-8

file_path = 'learning_python.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        new_line = line.replace('Python', 'Java')
        print(new_line)

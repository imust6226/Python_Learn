#coding = utf-8

file_path = 'learning_python.txt'

print("\nThe first time to read the file\n")
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents + '\n')

print("\nThe second time to read the file\n")
with open(file_path) as file_object:
    contents = file_object.readlines()
    for line in contents:
        print(line)
    

print("\nThe third time to read the file\n")
msgs = []
with open(file_path) as file_object:
    contents = file_object.readlines()
    for line in contents:
        msgs.append(line)
for msg in msgs:
    print(msg)

print(msgs)

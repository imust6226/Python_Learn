#coding = utf-8

file_path = 'guest.txt'

msg = input("Please input your name:\n")

with open(file_path, 'w') as file_object:
    file_object.write(msg)
    print("录入完毕")

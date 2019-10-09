#coding = utf-8

file_path = 'guest_book.txt'

while True:
    
    msg = input("Please input your name:\n")
    if msg != 'q':
        with open(file_path, 'a') as file_object:
            file_object.write(msg + '\n')
            print(msg + ',you are now in,welcome to the class.')
    else:
        break

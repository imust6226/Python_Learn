#coding = utf-8


file_path = 'code_reason.txt'

while True:
    msg = input("I'd like to ask your reason in coding,can you tell me?\n")
    if msg == 'Q':
        break
    elif msg == 'q':
        break
    elif msg == 'quit':
        break
    else:
        with open(file_path, 'a') as file_object:
            file_object.write(msg + '\n')
            print("Already Recorded!")

    

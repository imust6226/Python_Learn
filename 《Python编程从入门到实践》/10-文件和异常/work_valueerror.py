#coding = utf-8

class ValueErrorClass(object):
    def __init__(self):
        pass
    
    def value_error(self):
        while True:
            msg_one = input("Give me the first number:\n")
            if msg_one == 'q':
                break
            msg_two = input("Give me the second number:\n")
            if msg_two == 'q':
                break

            try:
                answer = int(msg_one) / int(msg_two)                
            except ZeroDivisionError:
                print("Zerro can't do this")
            except ValueError:
                print("Please give two numbers instead of words")
                #break
            else:
                print(answer)


var = ValueErrorClass()
var.value_error()

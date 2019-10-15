#coding = utf-8

def fun1():
    while True:
        msg = input("your age,please\n")
        if msg == 'q':
            break
        else:
            age = int(msg)
            if age < 3:
                print(str(age) + " years old for free.\n")
            elif age >=3 and age < 12:
                print(str(age) + " years old for ten dollars.\n")
            elif age >=12:
                print(str(age) + " years old for fivteen dollars.\n")
        
def fun2():
    active = True
    while active:
        msg = input("your age,please\n")
        if msg == 'q':
            active = False
        else:
            age = int(msg)
            if age < 3:
                print(str(age) + " years old for free.\n")
            elif age >=3 and age < 12:
                print(str(age) + " years old for ten dollars.\n")
            elif age >=12:
                print(str(age) + " years old for fivteen dollars.\n")

def fun3():
    active = True
    while active:
        msg = input("your age,please\n")
        if msg == 'quit':
            break
        else:
            age = int(msg)
            if age < 3:
                print(str(age) + " years old for free.\n")
            elif age >=3 and age < 12:
                print(str(age) + " years old for ten dollars.\n")
            elif age >=12:
                print(str(age) + " years old for fivteen dollars.\n")


fun3()
    

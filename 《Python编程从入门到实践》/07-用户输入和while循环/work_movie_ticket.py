#coding = utf-8

while True:
    msg = input("your age,please\n")
    age = int(msg)
    if age < 3:
        print(str(age) + " years old for free.\n")
    elif age >=3 and age < 12:
        print(str(age) + " years old for ten dollars.\n")
    elif age >=12:
        print(str(age) + " years old for fivteen dollars.\n")
    
    

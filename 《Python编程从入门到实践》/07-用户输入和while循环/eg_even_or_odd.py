#coding = utf-8

number = input("Enter a number,and I'll tell you if it's even or odd:")
number = int(number)

if number % 2 == 0:
    print("The Number " + str(number) + " is even")
else :
    print("The Number " + str(number) + " is odd")

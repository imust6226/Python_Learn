#coding = utf-8

height = input("How tall are you,in inches?")
#使用int()函数将字符型数字转化为整数型数字
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

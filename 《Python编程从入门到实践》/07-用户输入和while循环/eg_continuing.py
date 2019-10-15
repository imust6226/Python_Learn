#coding = utf-8

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        """如果能够被2整除，就继续下去，目的是打印小于10的奇数
        """
        continue

    print(current_number)

#coding = utf-8

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age <18:
    print("Your admission cost is $5.")
else :
    print("Your admission cost is $10.")

    
age = 15
if age < 4:
    price =0
elif age < 18:
    price = 5
else :
    price = 10

print("Your admission cost is $" + str(price) + ".")


age = 65
if age < 4:
    price =0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else :
    price = 5
    # 可以省略掉最后一个 else 语句，只保留到 elif 语句。
print("Your admission cost is $" + str(price) + ".")

#coding = utf-8

# 比较字符串
car = 'bMw'
print(car == 'Bmw')
print(car.lower() == 'bmw')

# 比较不等的时候
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies")
# 比较数字

age = 18
print(age == 19)

answer = 17
if answer != 42:
    print("That's not ths correct answer,please try again!")

print(age == 18)
print(age >= 17)
print(age <= 17)
print(age > 17)
print(age < 17)
print(age != 17)

# 还可以检查多个条件 使用 and 或者 or

print(age > 17 and age <= 18)
print(age > 17 or age < 18)

# 检查特定的值是否在列表中
requested_toppings = ['mushrooms', 'anchovies', 'pineapple']
use = 'apple'
if use in requested_toppings:
    print("yes,it's in.")


if use not in requested_toppings:
    print("yes， it's not in.")


# 布尔表达是
game_active = True
can_edit = False
print(game_active)
print(can_edit)

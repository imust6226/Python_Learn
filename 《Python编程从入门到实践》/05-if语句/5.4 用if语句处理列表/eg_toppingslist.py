#coding = utf-8

requested_toppings = ['mushrooms', 'extra cheese']


for requested_topping in requested_toppings :
    if requested_topping == 'green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("Finished making your pizza!\n")


# 确认列表不是空的
requested_toppings = []
if requested_toppings :
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?\n")

"""如果只想执行一个代码块就用 if-elif-else 结果，否则就用一些系列独立
的if语句"""


# 处理多个列表

requested_toppings = ['mushrooms', 'extra cheese','french fries','olives']
available_toppings = ['mushrooms', 'extra cheese','olives','green peppers',
                      'pepperoni','pineapple']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry,we don't have " + requested_topping + ".")
print("Finished making your pizza!\n")

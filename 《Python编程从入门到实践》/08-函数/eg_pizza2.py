#coding = utf-8


"""
    传递任意数量的形参和位置形参
    传入的任意数量实参，将实参封装进一个元组中
"""
def make_pizza(size, *toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a " + str(size) + " -inch pizza with the following toppings:")
    for topping in toppings:
        
        print("- " + topping)
    #print(type(toppings))

make_pizza(16, 'pepperoni')

make_pizza(12, 'pepperoni', 'green peppers', 'extra cheese')


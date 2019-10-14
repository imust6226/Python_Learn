#coding = utf-8


"""
    传递任意数量的实参
    传入的任意数量实参，将实参封装进一个元组中
"""
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        
        print("- " + topping)
    print(type(toppings))

make_pizza('pepperoni')

make_pizza('pepperoni', 'green peppers', 'extra cheese')  

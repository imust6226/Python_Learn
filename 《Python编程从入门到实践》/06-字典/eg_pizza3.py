#coding = utf-8


"""
    传递任意数量的形参和位置形参
    传入的任意数量实参，将实参封装进一个元组中
"""
pizza = {
    'crust': 'trick',
    'topping': ['mushrooms','extra cheese']
    }

# 概述一哈这个pizza
print("You ordered a " + pizza['crust'] +
      "-crust pizza" +
      "with following toppings:")

for topping in pizza['topping']:
    print("\t" + topping)



favourite_language = {
    'jen':['python','ruby'],
    'sarah':['c','java'],
    'edward':['ruby','go','python'],
    'phil':['python']
    }
for name ,languages in favourite_language.items():
    print("\n" + name.title() +"'s favourite language are:")
    for language in languages:
        print("\t" + language.title() )

#coding = utf-8



#导入模块，模块是扩展名为.py的文件

import eg_pizza2
#导入特定的函数
from eg_pizza import make_pizza

from eg_pizza import make_pizza as p

"""导入模块时，需要指定模块名去调用函数
   导入了模块的函数时，可以直接通过函数去调用
"""
eg_pizza2.make_pizza(16, 'pepperoni')

#通过模块名.函数名调用
eg_pizza2.make_pizza(10, 'pepperoni', 'mushroom', 'extra cheese')


#直接使用函数调用
make_pizza('pepperoni', 'mushroom', 'extra cheese')


#通过函数的别名调用
p('pepperoni', 'mushroom')

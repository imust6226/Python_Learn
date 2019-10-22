#coding = utf-8

# 使用 range() 函数可以轻松生成一系列的数字

for value in range(1,5):
    print(value)

# 使用 list()函数可以将 range()函数轻松转换为列表

numbers = list(range(1,5))
print(type(numbers))

# range() 函数可以指定步长

even_numbers = list(range(2,11,2))
print(even_numbers)

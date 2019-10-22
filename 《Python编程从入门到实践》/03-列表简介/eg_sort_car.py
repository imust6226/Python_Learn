#coding = utf-8

cars1 = ['bmw', 'audi', 'toyota', 'subaru']
# 调用 sort()方法对列表进行永久性排序
cars1.sort()
print(cars1)

# 调用 sorted()函数对列表临时排序
cars2 = ['bmw', 'audi', 'toyota', 'subaru']
cars = sorted(cars2)
print(cars)
# 原来的列表未排序
print(cars2)


# 使用 reverse()方法，永久性地修改列表元素的顺序

cars3 = ['bmw', 'audi', 'toyota', 'subaru']
cars3.reverse()
print(cars3)

# 确定列表的长度
cars4 = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars4))

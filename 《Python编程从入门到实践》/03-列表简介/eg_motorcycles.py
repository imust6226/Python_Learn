#coding = utf-8

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 修改列表的元素成功
motorcycles[0] = 'ducati'
print(motorcycles)


# 在列表中添加元素
motorcycles.append("honda")
print(motorcycles)


# 使用append()增加元素
motorcycle = []

motorcycle.append("honda")

motorcycle.append("yamaha")

motorcycle.append("suzuki")
print(motorcycle)

# 在列表中插入元素
motorcycle.insert(0, 'ducati')
print(motorcycle)

# 从列表中删除元素

del motorcycle[0]
print(motorcycle)

# 使用pop()方法弹出、也可以弹出任意位置的值
popped_motorcycle = motorcycle.pop()
print(popped_motorcycle)
print(motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki','bmw']
last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0)
print("The first owned " + first_owned )
print("The last owned " + last_owned)
print(motorcycles)


# 根据值来删除元素，使用 remove() 方法

motorcycles = ['honda', 'yamaha', 'suzuki','bmw']
motorcycles.remove("yamaha")
print(motorcycles)

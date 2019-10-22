#coding = utf-8

dimensions = (200, 50)
print(type(dimensions))
print(dimensions[0])
print(dimensions[1])

# 修改元组的值是被禁止的
# dimensions[0] = 270

# 遍历元组中所有的值
for dimension in dimensions:
    print(dimension)


# 重新给元组复制

dimensions = (200, 50)
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 200)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

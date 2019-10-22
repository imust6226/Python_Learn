#coding = utf-8

players = ['charles', 'martina', 'michael', 'florence', 'eli']
# 输入前面三名队员，始于0 止于3（不包含）
print(players[0:3])
# 提取第二到第四的队员
print(players[1:4])

# 指定结束的索引
print(players[:4])

# 指定开始的索引
print(players[2:])

# 返回后面N位，这样即使长度增加了，也会照样返回最后面的三位队员

print(players[-3:])

# 遍历切片
for value in players[-4:]:
    print("\t" + str(value))


"""复制列表，
    我们一般使用切片来复制一个列表，不指定起始和结束的索引值，这样可以
    任意修改列表而不会影响到另外的列表
"""
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append("ice cream")

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

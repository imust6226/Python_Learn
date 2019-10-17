#coding = utf-8

guests = ['mr a', 'mrs b', 'mrs c', 'mrs d', 'mr e']
msg = "I'd like to invite you to come to my party."
print(guests[4].title() + "," + msg)
print(guests[0].title() + "won't be able to come.")

# 修改列表的某个值
guests[0] = 'mr new'

# 向列表的每个人打印一句话
print(guests[0].title() + "," + msg)
print(guests[1].title() + "," + msg)

print(guests[2].title() + "," + msg)
print(guests[3].title() + "," + msg)
print(guests[4].title() + "," + msg)


# 添加更多的人
guests.insert(0, 'mrs instert')
guests.append('mr append')
print(guests)

# 删除一些人

del guests[2]
guests.remove('mrs d')
poper1 = guests.pop()
poper2 = guests.pop()
poper3 = guests.pop()
poper4 = guests.pop()


print(guests)

del guests[0]
print(guests)

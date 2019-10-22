#coding = utf-8

magicians = ['alice', 'david', 'carolina']

# 使用 for 来遍历列表
"""for循环时，magician是一个临时变量，存储列表中的每一个值"""

for magician in magicians:
    #print(magician)
    print(magician.title() + ",that's a great tick!\n ")
    print("I can't wait to see your next trick," + magician.title() + ".\n")

# 完成for 循环的时候打印结束语
print("Thank you,everyone. That was a great magic show!")

#coding = utf-8

sandwich_orders = ['A', 'pastrami', 'B', 'pastrami', 'C', 'pastrami', 'E', 'F']
finished_sandwiches = []


print("pastrami was sold out.")

while 'pastrami' in sandwich_orders:
    # 循环条件判断原列表是否为空，如果是空就停止循环
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    san = sandwich_orders.pop()
    finished_sandwiches.append(san)
print(sandwich_orders)
# 完成制作所有的三明治
print(finished_sandwiches)

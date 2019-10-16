#coding = utf-8

sandwich_orders = ['A', 'B', 'C', 'E', 'F']
finished_sandwiches = []

while sandwich_orders:
    # 循环条件判断原列表是否为空，如果是空就停止循环
    sand = sandwich_orders.pop()
        
    print("I made your tuna sandwich: " + sand+ ".")
    finished_sandwiches.append(sand)
print(sandwich_orders)
# 完成制作所有的三明治
print(finished_sandwiches)

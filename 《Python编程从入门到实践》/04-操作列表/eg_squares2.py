#coding = utf-8

digits = list(range(1,11))
# 分别计算最大值、最小值、平均值
print(min(digits))
print(max(digits))
print(sum(digits))


# 列表解析

squares = [value ** 2 for value in range(1,11)]
print(squares)


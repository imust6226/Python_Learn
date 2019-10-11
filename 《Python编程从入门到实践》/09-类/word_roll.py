#coding = utf-8

from random import randint

class Die():
    def __init__(self, side = 6):
        """初始化，属性值默认为6"""
        self.side = side

    def roll_die(self):
        """设置一个num来计数，到了10就停止循环"""
        num = 1
        while num <=10:
            read_num = randint(1, self.side)
            print("第 " + str(num) + "次结果是：" + str(read_num))
            num +=1

print("十面的骰子，投掷10次的结果如下：")
die1 = Die(10)
die1.roll_die()
print("二十面的骰子，投掷10次的结果如下：")        
die2 = Die(20)
die2.roll_die()

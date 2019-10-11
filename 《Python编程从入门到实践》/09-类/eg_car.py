#coding = utf-8

class Car(object):
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.oldmeter_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_oldmeter(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.oldmeter_reading) + " miles on it.")

    def update_oldmeter(self, mileage):
        """将里程表的读数设置为指定的值,不能回调值"""
        if mileage >= self.oldmeter_reading:
            
            self.oldmeter_reading = mileage
        else:
            print("You can't roll back an oldmeter!")

    def increment_oldmeter(self, miles):
        """将里程表的读数增加指定的量"""
        if miles >= 0:
            self.oldmeter_reading += miles
        else :
            print("Failure,You can't draw it back!")
        

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.oldmeter_reading = 23
my_new_car.update_oldmeter(24)
my_new_car.increment_oldmeter(-3)
my_new_car.read_oldmeter()


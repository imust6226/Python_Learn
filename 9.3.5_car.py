#coding = utf-8


# 使用Python 2.x的时候，父类请使用继承 object 类
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
        return long_name.title()

    def read_oldmeter(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.oldmeter_reading) + " miles on it.")

    def update_oldmeter(self, mileage):
        """
            将里程表读数设置为指定的值
            禁止将里程表读书往回调
        """
        if mileage > self.oldmeter_reading:
            self.oldmeter_reading = mileage
        else:
            print("You can't roll back an oldmeter.")

    def increase_oldmeter(self, miles):
        """将里程表读数增加到指定的量"""
        self.oldmeter_reading += miles

    def fill_gass_tank(self):
        pass

"""        
my_new_car = Car('audi', 'a4', 2016)
long_name = my_new_car.get_descriptive_name()
print(long_name)
my_new_car.read_oldmeter()

# 直接修改属性值
my_new_car.oldmeter_reading = 23
my_new_car.read_oldmeter()

# 通过方法修改属性值
my_new_car.update_oldmeter(22)
my_new_car.read_oldmeter()

# 通过方法增加属性值
my_new_car.increase_oldmeter(10)
my_new_car.read_oldmeter()

"""
class ElectricCar(Car):
    """电动车的独特之处,将实例用作于属性"""

    def __init__(self, make, model, year, battery):
        """初始化父类的属性"""
        #super().__init__(make, model, year)
        """
            python 2.x中的继承
        """
        super(ElectricCar, self).__init__(make, model, year)
        self.battery_size = battery
        self.battery = Battery(self.battery_size, 10)
        
    def fill_gas_tank(self):
        """电动汽车没有邮箱，重写父类的方法"""
        print("This car doesn't need a gas tank!")
      

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size, goRange = 100):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
        self.goRange = goRange

    def describle_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("*************下面这句，是我通过属性值调用方法的***********")
        print("This car has a "+ str(self.battery_size) + "-kWh battery.")
        print("\n")

    def describle_goRange(self):
        if self.goRange >= 100:
            print("合格")
        else:
            print("不合格")
   

# 创建实例
my_tesla = ElectricCar("tesla", "model s", 2016, 100)
my_tesla_name = my_tesla.get_descriptive_name()
print(my_tesla_name)
"""通过ElectricCar的实例my_tesla的属性battery，并调用方法"""
my_tesla.battery.describle_battery()
my_tesla.battery.describle_goRange()

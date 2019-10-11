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

    def fill_gas_tank(self):
        print("OK,gas is fully filled.")

class Battery():
    """抽象出来一个电池类，并将电池类作为属性"""
    def __init__(self, battery_size = 70):
        """初始化电池属性"""
        self.battery_size = battery_size

    def describle_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            rang = 240
        elif self.battery_size ==85:
            rang = 270

        msg = "This car can go approximately " + str(rang)
        msg += " miles on a full charge."
        print(msg)
    
        

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
            初始化父类的属性
            再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        """
            在Python 2.7中的继承稍有不同
            class Car(object)
                def __init__(self, make, model, year):
                    pass
            class ElectricCar(Car):
                def __init__(self, make, model, year):
                    super(ElectricCar, self).__init__(make, model, year)
        """
        self.battery = Battery()
        
    

    def fill_gas_tank(self):
        """重写父类的方法"""
        print("This car does'n need a gas tank!")
        

    
#my_new_car = Car('audi', 'a4', 2016)
my_new_car = ElectricCar('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.oldmeter_reading = 23
my_new_car.update_oldmeter(24)
my_new_car.increment_oldmeter(-3)
my_new_car.read_oldmeter()
#使用ElectricCar类的battery属性【Battery对象】
my_new_car.battery = Battery(85)
my_new_car.battery.describle_battery()
my_new_car.fill_gas_tank()
my_new_car.battery.get_range()


#coding = utf-8


# ʹ��Python 2.x��ʱ�򣬸�����ʹ�ü̳� object ��
class Car(object):
    """һ��ģ�������ļ򵥳���"""

    def __init__(self, make, model, year):
        """��ʼ����������������"""
        self.make = make
        self.model = model
        self.year = year
        self.oldmeter_reading = 0

    def get_descriptive_name(self):
        """�����������������Ϣ"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_oldmeter(self):
        """��ӡһ��ָ��������̵���Ϣ"""
        print("This car has " + str(self.oldmeter_reading) + " miles on it.")

    def update_oldmeter(self, mileage):
        """
            ����̱��������Ϊָ����ֵ
            ��ֹ����̱�������ص�
        """
        if mileage > self.oldmeter_reading:
            self.oldmeter_reading = mileage
        else:
            print("You can't roll back an oldmeter.")

    def increase_oldmeter(self, miles):
        """����̱�������ӵ�ָ������"""
        self.oldmeter_reading += miles

"""        
my_new_car = Car('audi', 'a4', 2016)
long_name = my_new_car.get_descriptive_name()
print(long_name)
my_new_car.read_oldmeter()

# ֱ���޸�����ֵ
my_new_car.oldmeter_reading = 23
my_new_car.read_oldmeter()

# ͨ�������޸�����ֵ
my_new_car.update_oldmeter(22)
my_new_car.read_oldmeter()

# ͨ��������������ֵ
my_new_car.increase_oldmeter(10)
my_new_car.read_oldmeter()

"""
class ElectricCar(Car):
    """�綯���Ķ���֮��"""

    def __init__(self, make, model, year):
        """��ʼ�����������"""
        #super().__init__(make, model, year)
        """
            python 2.x�еļ̳�
        """
        super(ElectricCar, self).__init__(make, model, year)
        self.battery_size = 70

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla_name = my_tesla.get_descriptive_name()
print(my_tesla_name)
my_tesla.update_oldmeter(22)
my_tesla.read_oldmeter()

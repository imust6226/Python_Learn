#coding = utf-8

class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type):
        """初始化两个属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印出属性值"""
        print("This Restaurant " + self.restaurant_name + "Run With " + self.cuisine_type)

    def open_restaurant(self):
        """打印出营业的消息"""
        print("We are now in service! Welcome.")

    def set_number_served(self, num):
        """设置就餐的人数"""
        if num >= self.number_served:
            self.number_served = num
        else:
            None

    def increment_number_served(self, num):
        """调整就餐的人数"""
        self.number_served += num
        
    def get_number_served(self):
        num = "Now the number of guests are " + str(self.number_served) + "."
        return num
    


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        """初始化子类"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['apple', 'orange', 'banana']
        
    def get_flavors(self):
        """获取flavors属性"""
        print("I can offer you these flavors below:")
        for flavor in self.flavors:
            print(flavor)

my_icecream_stand = IceCreamStand("Lovly IceCream", "Wonderfully")
my_icecream_stand.get_flavors()
        
        

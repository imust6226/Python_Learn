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
    


restaurant1 = Restaurant("SanWan", "fruites in all kinds")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
    

restaurant2 = Restaurant("HaiWan", "Sea Foods")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant2.set_number_served(10)

restaurant2.increment_number_served(12)
print(restaurant2.get_number_served())

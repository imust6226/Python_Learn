#coding = utf-8

class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type):
        """初始化两个属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印出属性值"""
        print("This Restaurant " + self.restaurant_name + "Run With " + self.cuisine_type)

    def open_restaurant(self):
        """打印出营业的消息"""
        print("We are now in service! Welcome.")


restaurant = Restaurant("SanWan", "fruites in all kinds")
restaurant.describe_restaurant()
restaurant.open_restaurant()
    

restaurant = Restaurant("HaiWan", "Sea Foods")
restaurant.describe_restaurant()
restaurant.open_restaurant()

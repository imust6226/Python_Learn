#coding =utf-8

class Pet():

    def __init__(self):
        pass

    def describle_pet(self, animal_type, pet_name = 'my pet'):
        """显示宠物的信息"""
        """默认值形参，给形参添加一个默认值"""
        print("\nI Hava a " + animal_type + ".")
        print("My " + animal_type + "'s name is " + pet_name.title() + ".")



pet = Pet()
pet.describle_pet(pet_name = "harry", animal_type = "hamster")

#调用有默认值形参的函数后，不需要指定形参的值了
pet.describle_pet(animal_type = "DOG")


pet.describle_pet("cat")

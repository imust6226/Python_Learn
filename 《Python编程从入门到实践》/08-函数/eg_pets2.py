#coding =utf-8

class Pet():

    def __init__(self):
        pass

    def describle_pet(self, animal_type, pet_name):
        """显示宠物的信息"""
        print("\nI Hava a " + animal_type + ".")
        print("My " + animal_type + "'s name is " + pet_name.title() + ".")


"""关键字实参，不再关心参数的位置"""
pet = Pet()
pet.describle_pet(pet_name = "harry", animal_type = "hamster")

pet.describle_pet(animal_type = "DOG", pet_name = "willian")



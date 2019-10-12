#coding =utf-8

class Pet():

    def __init__(self):
        pass

    def describle_pet(self, animal_type, pet_name):
        """显示宠物的信息"""
        print("\nI Hava a " + animal_type + ".")
        print("My " + animal_type + "'s name is " + pet_name.title() + ".")


pet = Pet()
pet.describle_pet("hamster", "harry")

pet.describle_pet("dog", "willie")

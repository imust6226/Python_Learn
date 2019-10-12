#coding = utf-8

class MakeShirt():

    def __init__(self):
        pass

    def make_shirt(self, size = "L", word_to_print = "L Love Python"):
        msg = ("\nThis Shirt you need is Size " + str(size)
              + " and your word is " + str(word_to_print))
        print(msg)

    def describle_city(self, city = "Reykjavik", contry = "Iceland"):
        msg =  "\n" + city.title() + "is in " + contry.title()
        print(msg)

makeshirt = MakeShirt()
makeshirt.make_shirt()

makeshirt.make_shirt(word_to_print = "Hello Word", size = "S")
makeshirt.describle_city()
makeshirt.describle_city("Akureyri")
makeshirt.describle_city("NewYork", contry = "USA")
makeshirt.describle_city(contry = "US", city = "London")
        

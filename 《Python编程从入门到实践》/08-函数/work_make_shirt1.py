#coding = utf-8

class MakeShirt():

    def __init__(self):
        pass

    def make_shirt(self, size, word_to_print):
        msg = ("This Shirt you need is Size " + str(size)
              + " and your word is " + str(word_to_print))
        print(msg)
    

makeshirt = MakeShirt()
makeshirt.make_shirt("M", "Hello")
        

        

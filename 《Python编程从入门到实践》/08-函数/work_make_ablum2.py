#coding = utf-8

class MakeAblum():

    def __init__(self):
        pass

    def make_ablum(self, singer, ablum, num = 10):
        """打印并返回字典"""
        cd = {'singer':singer.title(),'ablum':ablum.title(),'num':num}
        print(cd)
        return cd

    def while_can(self):
        while True:
            print("\nTell me the singer: ")
            print("Enter a 'q' to quit: ")
            singer = input("Singer: ")
            if singer == 'q':
                break
            ablum = input("Abluem: ")
            if ablum == 'q':
                break
            number = input("Number: ")
            if number and number != 'q':
                num = number
            elif number == 'q':
                break
            else:
                num = 10
            self.make_ablum(singer, ablum, num)

makeablum = MakeAblum()
makeablum.while_can()
    


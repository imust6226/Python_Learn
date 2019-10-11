#coding = utf-8

from collections import OrderedDict


class MyOrderedDict():

    def __init__(self):

        self.parm = OrderedDict()

    def record_parm(self):
        while True:
            msg = input("Your Name,Please:")
            if msg == "q":
                break
            ans = input("Your Favourite Language:")
            if ans == "q":
                break
            self.parm[msg] = ans
        return self.parm

    def show_parm(self):
        for name, language in self.parm.items():
            print(name.title() + "'s favourite language is " +
                  language.title() + ".")

ordereddict = MyOrderedDict()

ordereddict.record_parm()

ordereddict.show_parm()

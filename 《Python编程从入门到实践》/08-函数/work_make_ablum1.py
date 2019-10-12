#coding = utf-8

class MakeAblum():

    def __init__(self):
        pass

    def make_ablum(self, singer, ablum, num = 10):
        """打印并返回字典"""
        cd = {'singer':singer.title(),'ablum':ablum.title(),'num':num}
        print(cd)
        return cd

makeablum = MakeAblum()
makeablum.make_ablum(singer = "unknow", ablum = 'not here')
    
makeablum.make_ablum(singer = "unknow", ablum = 'not here', num =11)

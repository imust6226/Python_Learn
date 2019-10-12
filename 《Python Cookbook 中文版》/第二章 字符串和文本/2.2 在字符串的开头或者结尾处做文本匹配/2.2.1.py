#coding = utf-8


"""
startswith()
endswith()
做检查的时候需要传入的是元组类型，即tuple

"""

class StartEndWith():
    def __init__(self):
        pass



    def read_data(self, name, choice):
        if name.startswith(choice):
            print("Yes, StartsWith")
        else:
            print("No,StartsWith")
        if name.endswith(choice):
            print("Yes,EndsWith")
        else:
            print("No,EndsWith")

url = 'https://www.baidu.com'
choices = ['http:', 'https', 'ftp', 'ftps', 'cn', 'com', 'eduction']

start_or_end = StartEndWith()
start_or_end.read_data(name = url, choice = tuple(choices))

#coding = utf-8

import json

class ReadAndWrite():
    def __init__(self, numbers):
        self.numbers = numbers
        self.fileName = "D:\\1etrip系统\\tmp.txt"
        self.msg = "Successfully!"

    def number_write(self):
        try:
            with open(self.fileName, 'w') as file:
                json.dump(self.numbers, file)
        except FileNotFoundError:
            print("File Not Found,Please Check In Again!")
        else:
            print(self.msg)

    def number_read(self):
        try:
            with open(self.fileName) as file:
                json.load(file)
        except FileNotFoundError:
            print("File Not Found,Please Check In Again!")
        else:
            print(self.msg)

            
number = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 0]
rnw = ReadAndWrite(number)
rnw.number_write()
rnw.number_read()

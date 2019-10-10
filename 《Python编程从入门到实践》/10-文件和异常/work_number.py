#coding = utf-8

import json

class RememberNum(object):
    
    def __init__(self):
        self.filePath = 'number.json'

    def get_stored_number(self):
        try:
            with open(self.filePath) as f_obj:
                num = json.load(f_obj)
        except FileNotFoundError:
            pass
        except Exception:
            pass
        else:
            print("获取成功")
            return num

    def get_new_number(self):
        number = input("May I Have Your Favourite Number?\n")
        try:
            with open(self.filePath, 'w') as f_obj:
                json.dump(number, f_obj)
        except FileNotFoundError:
            print("Sorry,I don't Get The File")
          
        except Exception:
            print("Bad Things Happened!")
            
        else:
            return number

    def guess_number(self):
        num = self.get_stored_number()
        if num:
            print("That's your number " + num + '.')
        else:
            number = self.get_new_number()
            print("I do remember your number!")

rememberNum = RememberNum()
rememberNum.guess_number()
            

#coding = uft-8

import json

class RememberMe(object):

    def __init__(self):
        self.filePath = 'username.json'

    def areYouThere(self, file):
        try:
            with open(file) as f_obj:
                username = json.load(f_obj)
        except FileNotFoundError:
            username = input("What is your name?")
            with open(file, 'w') as f_obj:
                json.dump(username, f_obj)
                print("We'll remember you when you come back, " + username + "!")
        except Exception:
            print("Unknow Error!Something Must Went Wrong!")
        else:
            print("Welcome back, " + username + "!")
    


remember = RememberMe()
remember.areYouThere(remember.filePath)

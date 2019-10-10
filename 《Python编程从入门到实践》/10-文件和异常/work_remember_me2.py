#coding = uft-8

import json

class RememberMe(object):

    def __init__(self， name):
        self.filePath = 'username.json'
        self.name = name

    def get_stored_username(self):
        """如果储存有用户名，就读取出来"""
        try:
            with open(self.filePath) as f_obj:
                username = json.load(f_obj)
        except FileNotFoundError:
            pass
        except Exception:
            pass
        else:
            return username

    def get_new_username(self):
        """提示输入用户名"""
        username = input("What is your name?\n")
        try:
            with open(self.filePath, 'w') as f_obj:
                json.dump(username, f_obj)
        except FileNotFoundError:
            pass
        except Exception:
            pass
        else:
            return username

    def greet_user(self):
        """问候用户名"""
        username = self.get_stored_username()
        if username == self.name:
            print("Welcome back, " + username + "!")
        else:
            print("Sorry, I don't recongize you " + username + "Let me know your name,please.\n")
            username = self.get_new_username()
            print("We'll remember you when you come back, " + username + "!")
                
            
rememberme = RememberMe('Lcuy')
rememberme.greet_user()



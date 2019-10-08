#coding = utf-8

import json
"""json这个模块写或者读文件的时候，如果文件不存在，会自动创建一个文件"""

def get_stored_username():
    """如果储存了用户名就获取它"""
    fileName = "D:\\1etrip系统\\tmp1.txt"
    try:
        with open(fileName) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示输入用户名"""
    username = input("\nWhat's your name:\t")
    fileName = "D:\\1etrip系统\\tmp1.txt"
    with open(fileName, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def great_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back "+username+" !")
    else:
        username = get_new_username()
        print("We'll remember you when you come back "+username+" !")
    
great_user()

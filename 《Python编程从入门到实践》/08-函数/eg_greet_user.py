#coding = utf-8

def greet_users(names):
    """向列表中的每位用户都发出简单的问候语"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hanna', 'tyr', 'margot']
greet_users(usernames)

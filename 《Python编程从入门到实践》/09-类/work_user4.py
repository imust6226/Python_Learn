#coding = utf-8

class User(object):

    def __init__(self, first_name, last_name, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.sex = 'Male'
        self.degree = 'High School'
        self.carrer = 'Student'

    def describe_user(self):
        print("My name's " + self.first_name.title() + ' ' + self.last_name.title())
        print("I'm in " + self.degree + ',no more will tell you!')

    def greet_user(self):
        print("Welcome")


    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def get_login_attempts(self):
        msg = "The user now attemp to login, count = " + str(self.login_attempts) + "."
        return msg


class Priviliges():
    def __init__(self):
        self.priviliges = ["can add post", "can delete post", "can ban user"]

    def show_privilige(self):
        print("Here's My Priviliges.")
        for privilige in self.priviliges:
            print(privilige)

class Admin(User):

    def __init__(self, first_name, last_name):
        """父类有个默认的属性值，如果没有初始化则子类不具有这个属性"""
        super().__init__(first_name, last_name)
        self.anything = "It's Nothing."
        self.privilige = Priviliges()

    def anything_to_do(self):
        pass

    


admin = Admin("Lcuy", "Lily")
admin.privilige.show_privilige()

admin.describe_user()


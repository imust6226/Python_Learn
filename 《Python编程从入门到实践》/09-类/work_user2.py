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

user1 = User("Wang", "Liu")
user1.describe_user()
user1.greet_user()

user2 = User("Liu", "lensg")
user2.describe_user()
user2.greet_user()

user3 = User("lucy", "Liu", 3)
user3.describe_user()
user3.greet_user()
user3.increment_login_attempts()
print(user3.get_login_attempts())
user3.reset_login_attempts()
print(user3.get_login_attempts())




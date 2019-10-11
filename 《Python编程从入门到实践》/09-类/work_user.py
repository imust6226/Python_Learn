#coding = utf-8

class User(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = 'Male'
        self.degree = 'High School'
        self.carrer = 'Student'

    def describe_user(self):
        print("My name's " + self.first_name.title() + ' ' + self.last_name.title())
        print("I'm in " + self.degree + ',no more will tell you!')

    def greet_user(self):
        print("Welcome")


user1 = User("Wang", "Liu")
user1.describe_user()
user1.greet_user()

user2 = User("Liu", "lensg")
user2.describe_user()
user2.greet_user()

user3 = User("lucy", "Liu")
user3.describe_user()
user3.greet_user()

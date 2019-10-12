#coding = utf-8

class Greeter():

    def __init__(self, name = 'Stranger'):
        self.name = name

    def greet_user(self, name):
        if self.name.lower() != "stranger":
            print("Hello," + self.name.title() + ".")
        else :
            print("Hello, " + name.title() + ".")

print("greeter1 is calling.")
greeter1 = Greeter()
greeter1.greet_user("lily")
print("greeter2 is calling.")
greeter2 = Greeter('lucy')
greeter2.greet_user("lily")

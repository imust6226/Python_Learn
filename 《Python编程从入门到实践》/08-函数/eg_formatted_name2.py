#coding = utf-8


class FormattedName():

    def __init__(self):
        pass

    def get_formatted_name1(self, first, last):
        """没有中间名字，返回整洁的姓名"""
        full_name = first + " " + last
        return full_name.title()
        
    def get_formatted_name2(self, first, last, middle = ''):
        """返回整洁的姓名"""
        if middle:
            full_name = first + " " + middle + " " + last
        else:
            full_name = first + " " + last
        return full_name.title()
    def run_while(self):
        while True:
            print("\nPlease tell me your name:")
            print("Enter 'q' at any time to quit")
            f_name = input("first name: ")
            if f_name == 'q':
                break
            l_name = input("last name: ")
            if l_name == 'q':
                break
            full_name = self.get_formatted_name1(f_name, l_name)
            print("\n Hello," + full_name + ".")
name = FormattedName()
name.run_while()

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

name = FormattedName()
print(name.get_formatted_name2('jimi', 'hendrix'))
print(name.get_formatted_name2('john', 'lee', 'hooker'))

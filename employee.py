#coding = utf-8

class Employee():

    def __init__(self, second_name, first_name, salary_per_year):
        """初始化实例的属性"""
        self.second_name = second_name
        self.first_name = first_name
        self.salary_per_year = salary_per_year

    def getFullName(self):
        """获取雇员的姓名全称"""
        full_name = self.first_name + ' ' + self.second_name
        return full_name.title()

    def getSalaryForYear(self):
        """获取雇员增加后的年薪收入"""
        return self.salary_per_year

    def give_raise(self, salaryAdd = 5000):
        """
            给雇员增加年薪，设置默认增加的年薪
        """
        self.salary_per_year += salaryAdd
    

    

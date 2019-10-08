#coding = utf-8

class Employee(object):

    def __init__(self, first_name, last_name, salary_per_year):
        self.first_name = first_name
        self.last_name = last_name
        self.salary_per_year = salary_per_year

    def give_default_raise(self):
        self.salary_per_year += 40000

    def give_custom_raise(self, salary):
        self.salary_per_year += salary

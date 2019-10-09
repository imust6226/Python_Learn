#coding =utf-8

import unittest
from work_employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        """创建setUp()方法"""
        self.employee = Employee("Mary", "Hailen", 8920)

    def test_give_default_raise(self):
        """测试默认增加的年薪"""
        self.employee.give_raise()
        self.assertEqual(13920, self.employee.salary_per_year)

    def test_give_cuntom_raise(self):
        """测试正常增加的年薪"""
        self.employee.give_raise(4000)
        self.assertEqual(12920, self.employee.salary_per_year)
        
    def test_getSalaryForYear1(self):
        """测试实例的年薪"""
        self.employee.getSalaryForYear()
        self.assertEqual(8920, self.employee.salary_per_year)

    def test_getSalaryForYear2(self):
        """测试获得增加后的年收入"""
        self.employee.give_raise(6000)
        self.assertEqual(14920, self.employee.salary_per_year)
        
    def test_getFullName(self):
        """测试获取雇员姓名全称"""
        fullName = self.employee.getFullName()
        self.assertEqual("Hailen Mary", fullName)

if __name__ == "__main__":
    unittest.main()

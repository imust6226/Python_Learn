#coding = utf-8

import unittest
from work11_3 import Employee

class TestWorkTestCase(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("markin", "lucy", 60000)

    def test_give_default_raise(self):
        self.employee.give_default_raise()
        self.assertEqual(100000, self.employee.salary_per_year)

    def test_give_custom_raise(self):
        self.employee.give_custom_raise(salary = 50000)
        self.assertEqual(110000, self.employee.salary_per_year)

    def test_give_custom_raise2(self):
        self.employee.give_custom_raise(salary = 51000)
        self.assertNotEqual(self.employee.salary_per_year, 100000)

if __name__ == "__main__":
    unittest.main()

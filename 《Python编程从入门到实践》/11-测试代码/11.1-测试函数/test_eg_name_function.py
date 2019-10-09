#coding = utf-8

import unittest
from eg_name_function import get_formatted_name1,get_formatted_name2,get_formatted_name3

"""
    对函数进行测试
    1、创建一个测试类，对函数进行测试
    2、这个测试类必须继承自 unittest.TestCase 类
"""

class NamesTestCase(unittest.TestCase):
    """测试 eg_name_function.py"""

    def test_get_formatted_name1_1(self):
        """能够正确地处理像Janis Joplin这样子的姓名么？"""
        formattedName = get_formatted_name1('janis', 'joplin')
        self.assertEqual(formattedName, 'Janis Joplin')

    def test_get_formatted_name1_2(self):
        """能够正确地处理像Janis Joplin这样子的姓名么？"""
        formattedName = get_formatted_name1('jANis', 'joplin')
        self.assertEqual(formattedName, 'Janis Joplin')

    def test_get_formatted_name2_1(self):
        """能够正确地处理像Janis Dom Joplin这样子的姓名么？"""
        formattedName = get_formatted_name2('janis', 'joplin', 'dom')
        self.assertEqual(formattedName, 'Janis Dom Joplin')

    def test_get_formatted_name2_2(self):
        """能够正确地处理像Janis Dom Joplin这样子的姓名么？"""
        formattedName = get_formatted_name2('janis', 'joplin', 'DOM')
        self.assertNotEqual(formattedName, 'Janis DOM Joplin')
    
    def test_get_formatted_name3_1(self):
        """能够正确地处理像Janis Dom Joplin这样子的姓名么？"""
        formattedName = get_formatted_name3('janis', 'joplin', 'dom')
        self.assertEqual(formattedName, 'Janis Dom Joplin')

    def test_get_formatted_name3_2(self):
        """能够正确地处理像Janis Joplin这样子的姓名么？"""
        formattedName = get_formatted_name3('janis', 'joplin')
        self.assertEqual(formattedName, 'Janis Joplin')
        


if __name__ == '__main__':
    unittest.main()

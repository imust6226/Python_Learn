#coding = utf-8

import unittest
from name_function import get_formatted_name

class NamsTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确的处理像Janis Joplin这样子的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确的处理像Janis Joplin这样子的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin', 'lourla')
        self.assertEqual(formatted_name, 'Janis Lourla Joplin')
        
    def test_first_last_name_failour(self):
        """能够正确的处理像Janis Joplin这样子的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin', 'lourla')
        self.assertNotEqual(formatted_name, 'Janis lourla Joplin')

if __name__ == '__main__':
    unittest.main()

#coding = utf-8

import unittest
from city_functions import city_country,city_country2,city_country3

class city_countryTestCase(unittest.TestCase):
    """测试city_country()方法"""

    def test_city_countries1(self):
        message = city_country("beiJing","chinA")
        self.assertEqual(message,"Beijing,China")
        
    def test_city_countries2(self):
        message = city_country("CHONGQING","CHINA")
        self.assertEqual(message,"Chongqing,China")

    def test_city_country2_1(self):
        message = city_country2("hebei")
        self.assertEqual(message, "Hebei,China")

    def test_city_country2_2(self):
        message = city_country2("santiago", "chile")
        self.assertEqual(message, "Santiago,Chile")

    def test_city_country2_3(self):
        message = city_country2("HeBei", "China")
        self.assertEqual(message, "Hebei,China")

    def test_city_country3_1(self):
        message = city_country3("santiago", "chile", population = "10w")
        self.assertEqual(message, "Santiago,Chile - population 10w")

    def test_city_country3_2(self):
        message = city_country3("santiago", "chile")
        self.assertEqual(message, "Santiago,Chile - population 50w")
        
    def test_city_country3_3(self):
        message = city_country3("santiago", country = "chile")
        self.assertEqual(message, "Santiago,Chile - population 50w")

if __name__ == "__main__":
    unittest.main()

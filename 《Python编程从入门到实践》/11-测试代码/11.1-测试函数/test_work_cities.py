#coding = uft-8

import unittest
from cities import city_contry,city_contry_population1,city_contry_population2

class CitiesTestCase(unittest.TestCase):

    def test_city_contry1_1(self):
        """能够正常返回 Santiago,Chile"""
        cityMsg_formatted = city_contry('santiago', 'chile')
        self.assertEqual(cityMsg_formatted, 'Santiago,Chile')

    def test_city_contry1_2(self):
        """能够正常返回 Santiago,Chile"""
        cityMsg_formatted = city_contry('SANTIAGO', 'chile')
        self.assertEqual(cityMsg_formatted, 'Santiago,Chile')

    def test_city_contry_population1_1(self):
        """能够正常返回 Santiago,Chile - population 2000000"""
        cityMsg_formatted = city_contry_population1('santiago', 'chile', 2000001)
        self.assertEqual(cityMsg_formatted, 'Santiago,Chile - Population 2000001')
    
        
    def test_city_contry_population2_1(self):
        """能够正常返回 Santiago,Chile - population 2000000"""
        cityMsg_formatted = city_contry_population2('santiago', 'chile', 2000000)
        self.assertEqual(cityMsg_formatted, 'Santiago,Chile - Population 2000000')
                         
    def test_city_contry_population2_2(self):
        """能够正常返回 Santiago,Chile - population No Data"""
        cityMsg_formatted = city_contry_population2('santiago', 'chilE')
        self.assertEqual(cityMsg_formatted, 'Santiago,Chile - Population No Data')


if __name__ == '__main__':
    unittest.main()

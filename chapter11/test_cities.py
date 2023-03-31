from city_functions import cities
import unittest

class citiy_test(unittest.TestCase):
    """test for cities function"""
    def test_cities(self):
        formated_city = cities('khartoum', 'sudan', 80000)
        self.assertEqual(formated_city, 'Khartoum, Sudan population 80000')
        formated_city = cities('london', 'uk')
        self.assertEqual(formated_city, 'London, Uk')

if __name__ == '__main__':
    unittest.main()
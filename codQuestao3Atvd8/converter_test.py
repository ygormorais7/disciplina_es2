import unittest
from converter import celsius_to_fahrenheit

class TestTemperatureConversion(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

if __name__ == '__main__':
    unittest.main()


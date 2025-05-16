import unittest
from src.conversion import convertir_temperatura

class TestConversion(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(convertir_temperatura(0, "Celsius", "Fahrenheit"), 32)

    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(convertir_temperatura(32, "Fahrenheit", "Kelvin"), 273.15, places=2)

if __name__ == '__main__':
    unittest.main()

import unittest

from Converter import Converter


class TestConverter(unittest.TestCase):


    def setUp(self):
        self.testObj = Converter()

    def test_constructor(self):
        self.assertIsNotNone(self.testObj)

    def test_properties(self):
        self.assertEqual(self.testObj.temp_to_convert, -40.0)
        self.assertEqual(self.testObj.converted_temp, -40.0)

    def test_tempToConvert(self):
        self.testObj.setTemp(212.0)
        self.assertEqual(self.testObj.temp_to_convert, 212.0)

    def test_toCelsius(self):
        self.testObj.setTemp(212.0)
        self.testObj.toCelsius()
        self.assertEqual(self.testObj.temp_to_convert, 212.0)
        self.assertEqual(self.testObj.converted_temp, 100.0)

    def test_toFahrenheit(self):
        self.testObj.setTemp(100.0)
        self.testObj.toFahrenheit()
        self.assertEqual(self.testObj.temp_to_convert, 100.0)
        self.assertEqual(self.testObj.converted_temp, 212.0)

    def test_test(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
import unittest

from models.calculator import calculate


class CalculatorTest(unittest.TestCase):
    def test_suma_dos_numeros(self):
        self.assertEqual(calculate("2 + 3"), 5)

    def test_suma_numeros_mayores(self):
        self.assertEqual(calculate("10 + 5"), 15)

    def test_suma_decimales(self):
        self.assertEqual(calculate("2.5 + 1.5"), 4)


if __name__ == "__main__":
    unittest.main()

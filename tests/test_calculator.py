import unittest

from models.calculator import calculate


class CalculatorTest(unittest.TestCase):
    def test_suma_dos_numeros(self):
        self.assertEqual(calculate("2 + 3"), 5)

    def test_suma_numeros_mayores(self):
        self.assertEqual(calculate("10 + 5"), 15)

    def test_suma_decimales(self):
        self.assertEqual(calculate("2.5 + 1.5"), 4)

    def test_resta_dos_numeros(self):
        self.assertEqual(calculate("8 - 3"), 5)

    def test_numero_negativo_al_inicio(self):
        self.assertEqual(calculate("-5 + 3"), -2)

    def test_resta_con_numero_negativo(self):
        self.assertEqual(calculate("5 - -2"), 7)

    def test_multiplicacion_dos_numeros(self):
        self.assertEqual(calculate("4 * 3"), 12)

    def test_division_dos_numeros(self):
        self.assertEqual(calculate("10 / 2"), 5)

    def test_division_con_decimal(self):
        self.assertEqual(calculate("5 / 2"), 2.5)

    def test_division_entre_cero(self):
        self.assertEqual(calculate("8 / 0"), "Math Error")


if __name__ == "__main__":
    unittest.main()

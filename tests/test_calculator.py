import math
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

    def test_multiplicacion_antes_de_suma(self):
        self.assertEqual(calculate("2 + 3 * 4"), 14)

    def test_division_antes_de_resta(self):
        self.assertEqual(calculate("10 - 6 / 2"), 7)

    def test_operaciones_mismo_nivel_de_izquierda_a_derecha(self):
        self.assertEqual(calculate("20 / 5 * 2"), 8)

    def test_parentesis_cambian_la_precedencia(self):
        self.assertEqual(calculate("(2 + 3) * 4"), 20)

    def test_parentesis_en_medio_de_expresion(self):
        self.assertEqual(calculate("10 / (3 + 2)"), 2)

    def test_parentesis_anidados(self):
        self.assertEqual(calculate("2 * (3 + (4 - 1))"), 12)

    def test_potencia_dos_numeros(self):
        self.assertEqual(calculate("2 ^ 3"), 8)

    def test_potencia_antes_de_multiplicacion(self):
        self.assertEqual(calculate("2 * 3 ^ 2"), 18)

    def test_potencias_se_resuelven_de_derecha_a_izquierda(self):
        self.assertEqual(calculate("2 ^ 3 ^ 2"), 512)

    def test_porcentaje_simple(self):
        self.assertEqual(calculate("50%"), 0.5)

    def test_porcentaje_dentro_de_multiplicacion(self):
        self.assertEqual(calculate("200 * 10%"), 20)

    def test_porcentaje_en_una_expresion(self):
        self.assertEqual(calculate("1 + 50%"), 1.5)

    def test_constante_pi(self):
        self.assertEqual(calculate("pi"), math.pi)

    def test_pi_dentro_de_una_expresion(self):
        self.assertEqual(calculate("2 * pi"), 2 * math.pi)

    def test_pi_con_parentesis(self):
        self.assertEqual(calculate("pi * (2 + 1)"), 3 * math.pi)

    def test_raiz_cuadrada(self):
        self.assertEqual(calculate("sqrt(9)"), 3)

    def test_raiz_cuadrada_dentro_de_expresion(self):
        self.assertEqual(calculate("2 + sqrt(16)"), 6)

    def test_raiz_cuadrada_negativa(self):
        self.assertEqual(calculate("sqrt(-4)"), "Math Error")

    def test_seno_en_grados(self):
        self.assertAlmostEqual(calculate("sin(30)"), 0.5)

    def test_coseno_en_grados(self):
        self.assertAlmostEqual(calculate("cos(60)"), 0.5)

    def test_tangente_en_grados(self):
        self.assertAlmostEqual(calculate("tan(45)"), 1)

    def test_trigonometria_dentro_de_expresion(self):
        self.assertAlmostEqual(calculate("2 * sin(30)"), 1)

    def test_logaritmo_base_diez(self):
        self.assertEqual(calculate("log(100)"), 2)

    def test_logaritmo_natural(self):
        self.assertEqual(calculate("ln(1)"), 0)

    def test_logaritmo_de_cero(self):
        self.assertEqual(calculate("log(0)"), "Math Error")

    def test_logaritmo_natural_negativo(self):
        self.assertEqual(calculate("ln(-2)"), "Math Error")


if __name__ == "__main__":
    unittest.main()

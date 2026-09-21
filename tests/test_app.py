import unittest

from app import app


class CalculatorApiTest(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_suma_basica(self):
        res = self.client.post("/calculate", json={"expression": "2+3"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["result"], 5)

    def test_expresion_con_funciones(self):
        res = self.client.post("/calculate", json={"expression": "sqrt(16)+sin(30)"})
        self.assertEqual(res.status_code, 200)
        self.assertAlmostEqual(res.get_json()["result"], 4.5)

    def test_division_entre_cero(self):
        res = self.client.post("/calculate", json={"expression": "8/0"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["result"], "Math Error")

    def test_error_de_sintaxis(self):
        res = self.client.post("/calculate", json={"expression": "2 & 3"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["result"], "Syntax Error")

    def test_expresion_vacia(self):
        res = self.client.post("/calculate", json={"expression": ""})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["result"], "Syntax Error")

    def test_overflow_no_causa_error_500(self):
        res = self.client.post("/calculate", json={"expression": "1000 ^ 1000"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["result"], "Math Error")

    def test_cuerpo_malformado(self):
        res = self.client.post(
            "/calculate", data="no-json", content_type="application/json"
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["result"], "Syntax Error")

    def test_cuerpo_ausente(self):
        res = self.client.post("/calculate")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["result"], "Syntax Error")


if __name__ == "__main__":
    unittest.main()

import unittest
from myservice import app

app.testing = True

# TODO: Extend these component tests for the calc view
#       and THEN implement all 4 operations!
# DO NOT REMOVE EXISTING TESTS!


class TestCalc(unittest.TestCase):
    # Sum testing
    def test_sum1(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sum?m=3&n=5").get_json()
        self.assertEqual(reply["result"], "8")

    def test_sum2(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sum?m=5&n=-3").get_json()
        self.assertEqual(reply["result"], "2")

    def test_sum3(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sum?m=-5&n=3").get_json()
        self.assertEqual(reply["result"], "-2")

    def test_sum4(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sum?m=20&n=0").get_json()
        self.assertEqual(reply["result"], "20")

    def test_sum5(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sum?m=-500000&n=-500000").get_json()
        self.assertEqual(reply["result"], "-1000000")

    # Sub testing

    def test_sub1(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sub?m=3&n=5").get_json()
        self.assertEqual(reply["result"], "-2")

    def test_sub2(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sub?m=5&n=-3").get_json()
        self.assertEqual(reply["result"], "8")

    def test_sub3(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sub?m=-5&n=3").get_json()
        self.assertEqual(reply["result"], "-8")

    def test_sub4(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sub?m=20&n=0").get_json()
        self.assertEqual(reply["result"], "20")

    def test_sub5(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sub?m=-500000&n=-500000").get_json()
        self.assertEqual(reply["result"], "0")

    # Mul testing
    def test_mul1(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/mul?m=3&n=5").get_json()
        self.assertEqual(reply["result"], "15")

    def test_mul2(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/mul?m=-3&n=5").get_json()
        self.assertEqual(reply["result"], "-15")

    def test_mul3(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/mul?m=-3&n=-8").get_json()
        self.assertEqual(reply["result"], "24")

    def test_mul4(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/mul?m=4&n=0").get_json()
        self.assertEqual(reply["result"], "0")

    # Div testing
    def test_div1(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/div?m=3&n=0").get_json()
        self.assertEqual(reply["result"], "DivisionByZeroError")

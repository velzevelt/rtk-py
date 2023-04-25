from fraction import Fraction
import unittest

class TestFractionLogic(unittest.TestCase):
    def test_add(self):
        frac = Fraction(1, 2)
        frac2 = Fraction(3, 5)
        self.assertEqual(frac + frac2, Fraction(11, 10)) # 11/10 <- 5/10 + 6/10 <- 1/2 + 3/5

    def test_sub(self):
        frac = Fraction(1, 2)
        frac2 = Fraction(3, 5)
        self.assertEqual(frac - frac2, Fraction(-1, 10)) # -1/10 <- 5/10 - 6/10 <- 1/2 - 3/5

    def test_mul(self):
        frac = Fraction(1, 2)
        frac2 = Fraction(3, 5)
        self.assertEqual(frac * frac2, Fraction(3, 10)) # 3/10 <- 1*3/2*5 <- 1/2 * 3/5

    def test_div(self):
        frac = Fraction(1, 2)
        frac2 = Fraction(3, 5)
        self.assertEqual(frac / frac2, Fraction(5, 6)) # 5/6 <- 1*5/2*3 <- 1/2 * 5/3 <- 1/2 / 3/5

    def test_simplify(self):
        frac3 = Fraction(3, 12).simplify()
        self.assertEqual(frac3, Fraction(1, 4)) # 1/4 <- 3/12

        frac3 = Fraction(12, 3).simplify()
        self.assertEqual(frac3, Fraction(4, 1)) # 4/1 <- 12/3

        frac3 = Fraction(32, 6).simplify()
        self.assertEqual(frac3, Fraction(16, 3)) # 16/3 <- 32/6

        frac3 = Fraction(6, 32).simplify()
        self.assertEqual(frac3, Fraction(3, 16)) # 3/16 <- 6/32

        frac3 = Fraction(16, 20)
        self.assertEqual(frac3.simplify(), Fraction(4, 5))

    def test_zero_division(self):
        try:
            Fraction(1, 0)
        except ZeroDivisionError:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
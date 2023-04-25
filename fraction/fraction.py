import unittest

class Fraction:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, value):
        if value == 0:
            raise ZeroDivisionError
        self._denominator = value

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, value):
        self._numerator = value

    # Overload +, += operator
    def __add__(self, other):
        new_num = other.denominator * self.numerator
        new_num += other.numerator * self.denominator
        new_denom = other.denominator * self.denominator
        return Fraction(new_num, new_denom)

    # Overload -, -= operator
    def __sub__(self, other):
        new_num = other.denominator * self.numerator
        new_num -= other.numerator * self.denominator
        new_denom = other.denominator * self.denominator
        return Fraction(new_num, new_denom)

    # Overload / operator
    def __truediv__(self, other):
        return self * Fraction(other.denominator, other.numerator)

    # Overload // operator
    def __floordiv__(self, other):
        raise NotImplementedError

    # Overload * operator
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    # Overload == operator
    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    # Overload != operator
    def __ne__(self, other):
        return not self == other

    # Overload >= operator
    def __ge__(self, other):
        return self.numerator / self.denominator >= other.numerator / self.denominator

    # Overload > operator
    def __gt__(self, other):
        return self.numerator / self.denominator > other.numerator / self.denominator

    # Overload <= operator
    def __le__(self, other):
        return not self >= other

    # Overload < operator
    def __lt__(self, other):
        return not self > other

    # Overload string out
    def __str__(self):
        sign = '-' if not self.is_positive() else ''
        return f'{sign}{abs(self.numerator)}/{abs(self.denominator)}'

    def is_positive(self):
        frac = (self.numerator, self.denominator)
        return all(x >= 0 for x in frac) or all(x <= 0 for x in frac)

    def simpify(self):
        if self.denominator % self.numerator == 0:
            new_num = 1
            new_denom = self.denominator // self.numerator
            self.numerator = new_num
            self.denominator = new_denom
        elif self.numerator % self.denominator == 0:
            new_num = self.numerator // self.denominator
            new_denom = 1
            self.numerator = new_num
            self.denominator = new_denom
        elif self.numerator % 2 == 0 and self.denominator % 2 == 0:
            new_num = self.numerator // 2
            new_denom = self.denominator // 2
            while new_num % 2 == 0 and new_denom % 2 == 0:
                new_num = self.numerator // 2
                new_denom = self.denominator // 2
            self.numerator = new_num
            self.denominator = new_denom

        return self


def test():
    # import unittest

    class TestFractionLogic(unittest.TestCase):
        frac = Fraction(1, 2)
        frac2 = Fraction(3, 5)

        def test_add(self):
            self.assertEqual(frac + frac2, Fraction(11, 10)) # 11/10 <- 5/10 + 6/10 <- 1/2 + 3/5

        def test_sub(self):
            self.assertEqual(frac - frac2, Fraction(-1, 10)) # -1/10 <- 5/10 - 6/10 <- 1/2 - 3/5

        def test_mul(self):
            self.assertEqual(frac * frac2, Fraction(3, 10)) # 3/10 <- 1*3/2*5 <- 1/2 * 3/5

        def test_div(self):
            self.assertEqual(frac / frac2, Fraction(5, 6)) # 5/6 <- 1*5/2*3 <- 1/2 * 5/3 <- 1/2 / 3/5

        def test_simpify(self):
            frac3 = Fraction(3, 12).simpify()
            self.assertEqual(frac3, Fraction(1, 4)) # 1/4 <- 3/12

            frac3 = Fraction(12, 3).simpify()
            self.assertEqual(frac3, Fraction(4, 1)) # 4/1 <- 12/3

            frac3 = Fraction(32, 6).simpify()
            self.assertEqual(frac3, Fraction(16, 3)) # 16/3 <- 32/6

            frac3 = Fraction(6, 32).simpify()
            self.assertEqual(frac3, Fraction(3, 16)) # 3/16 <- 6/32

        def test_zero_division(self):
            self.assertRaises(ZeroDivisionError, Fraction(1, 0))

    t = unittest.main()


def interactive():
    pass


if __name__ == '__main__':
    test()
    interactive()

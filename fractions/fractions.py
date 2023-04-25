
class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError

        self.numerator = numerator
        self.denominator = denominator


    # +
    def __add__(self, other):
        self.numerator *= other.denominator
        self.numerator += other.numerator * self.denominator
        self.denominator *= other.denominator

        return self

    # -
    def __sub__(self, other):
        pass

    # /
    def __truediv__(self, other):
        pass

    # *
    def __mul__(self, other):
        pass

    # -self
    def __neg__(self):
        pass

    def __pos__(self):
        pass

    def __invert__(self):
        pass



def main():
    frac = Fraction(1, 2)
    frac2 = Fraction(3, 5)

    frac3 = frac + frac2

    print(frac3.numerator, frac3.denominator)


if __name__ == '__main__':
    main()
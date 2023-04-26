class Fraction:
    def __init__(self, numerator, denominator=1):
        if isinstance(numerator, float):
            frac = Fraction.convert(numerator)
            self.numerator = frac.numerator
            self.denominator = frac.denominator
        else:
            self.numerator = int(numerator)
            self.denominator = int(denominator)

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
        other = Fraction.convert(other)  

        new_num = other.denominator * self.numerator
        new_num += other.numerator * self.denominator
        new_denom = other.denominator * self.denominator
        return Fraction(new_num, new_denom)

    # Overload -, -= operator
    def __sub__(self, other):
        other = Fraction.convert(other)

        new_num = other.denominator * self.numerator
        new_num -= other.numerator * self.denominator
        new_denom = other.denominator * self.denominator
        return Fraction(new_num, new_denom)

    # Overload / operator
    def __truediv__(self, other):
        return self * Fraction(other.denominator, other.numerator)

    # Overload // operator
    def __floordiv__(self, other):
        return self / other

    # Overload * operator
    def __mul__(self, other):
        other = Fraction.convert(other)

        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    # Overload == operator
    def __eq__(self, other):
        other = Fraction.convert(other)
        
        return str(self) == str(other)

    # Overload != operator
    def __ne__(self, other):
        return not self == other

    # Overload >= operator
    def __ge__(self, other):
        other = Fraction.convert(other)

        return self.numerator / self.denominator >= other.numerator / self.denominator

    # Overload > operator
    def __gt__(self, other):
        other = Fraction.convert(other)

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

    def simplify(self):
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
                new_num //= 2
                new_denom //= 2
            self.numerator = new_num
            self.denominator = new_denom

        return self
    
    def convert(obj):
        if not isinstance(obj, Fraction):
            if isinstance(obj, float):
                tens = pow(10, fractional_part_len(obj))
                num = int(obj * tens)
                obj = Fraction(num, tens)
            else:
                obj = int(obj)  # Cannot cast from all types
                obj = Fraction(numerator=obj)
        return obj
    
    def to_float(self):
        return self.numerator / self.denominator


def fractional_part_len(number_to_count):
    count = 0
    
    while number_to_count % 1 != 0:
        number_to_count *= 10
        count += 1
    
    return count


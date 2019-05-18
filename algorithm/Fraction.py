def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


class Fraction(object):
    def __init__(self, num = 0, den = 1):
        if den == 0:
            exit('分母为0')
        if den < 0:
            num = -num
            den = -den
        g = gcd(num, den)
        self.num = num / g
        self.den = den / g

    def __add__(self, other): return Fraction(self.num * other.den + self.den * other.num, self.den * other.den)

    def __sub__(self, other): return Fraction(self.num * other.den - self.den * other.num, self.den * other.den)

    def __str__(self):
        if self.num == 0:
            return '0'
        if abs(self.num) == abs(self.den):
            return '1' if self.num > 0 else '-1'
        else:
            return str(self.num) + '/' + str(self.den)


if __name__ == '__main__':
    print(7 % 4)
    print(Fraction(1, 2) + Fraction(1, 2))


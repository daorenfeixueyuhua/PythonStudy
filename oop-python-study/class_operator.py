class Complex:

    # a 实部 b 虚部
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 等于运算符
    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        else:
            return False

    # 小于运算符
    def __lt__(self, other):
        if self.a < other.a:
            return True
        if self.a > other.a:
            return False
        if self.a == other.a:
            if self.b < other.b:
                return True
            if self.b > other.b:
                return False
            if self.b == other.b:
                return False

    # 大于运算符
    def __gt__(self, other):
        if self.a > other.a:
            return True
        if self.a < other.a:
            return False
        if self.a == other.a:
            if self.b > other.b:
                return True
            if self.b < other.b:
                return False
            if self.b == other.b:
                return False

    # 比较运算符
    def __cmp__(self, other):
        if self.a > other.a:
            return 1
        elif self.a == other.a:
            if self.b > other.b:
                return 1
            elif self.b == self.b:
                return 0
            else:
                return -1
        else:
            return -1

    # 相加
    def __add__(self, other):
        c = Complex(0, 0)
        c.a = self.a + other.a
        c.b = self.b + other.b
        return c

    # 相减
    def __sub__(self, other):
        c = Complex(0, 0)
        c.a = self.a - other.a
        c.b = self.b - other.b
        return c

    # 相乘
    def __mul__(self, other):
        c = Complex(0, 0)
        c.a = self.a * other.a - self.b * other.b
        c.b = self.a * other.b + self.b * other.a
        return c

    def __str__(self):
        return "%s + %di" % (self.a, self.b)


if __name__ == '__main__':
    c1 = Complex(1,2)
    c2 = Complex(1,2)

    if c1.__cmp__(c2) == 0:
        print("c1 和 c2 相等")
    elif c1.__cmp__(c2) == 1:
        print("c1 比较大哦")
    else:
        print("c2 比较大哦")

    add_c = c1.__add__(c2)
    print("c1 + c2 等于: ", add_c)

    sub_c = c1.__sub__(c2)
    print("c1 - c2 等于: ", sub_c)

    mul_c = c1.__mul__(c2)
    print("c1 * c2 等于: ", mul_c)
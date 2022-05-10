import  random

class EllipticalCurve:
    def __init__(self, a, b, p):
        if 4*a**3 + 27*b**2 == 0:
            raise Exception(f'x^3 + {a}x + {b} is singular')

        self.a = a
        self.b = b
        self.p = p

        generators = []
        for x in range(self.p):
            for y in range(self.p):
                if (x**3 + self.a*x + self.b - y**2) % self.p == 0:
                    generators.append((x, y))

        self.generators = generators
        self.g = generators[-1]

    def add(self, x, y):
        return (x % self.p + y % self.p) % self.p

    def sub(self, x, y):
        return (x % self.p - y % self.p) % self.p

    def mul(self, x, y):
        res = 0
        for i in range(y):
            res = self.add(res, x)
        return res


curve = EllipticalCurve(0, 7, 17)
print('generator: ', curve.g)

private_a = 13
public_a = (curve.mul(private_a, curve.g[0]), curve.mul(private_a, curve.g[1]))
print('public A: ', public_a)

private_b = 11
public_b = (curve.mul(private_b, curve.g[0]), curve.mul(private_b,curve.g[1]))
print('public B: ', public_b)

m = (3, 4)
k = random.randint(1, 10)
c = [
    (curve.mul(k, curve.g[0]), curve.mul(k, curve.g[1])),
    (curve.add(m[0], curve.mul(k, public_b[0])), curve.add(m[1], curve.mul(k,public_b[1])))
]
print('cipher:', c)

c0 = c[0]
c1 = c[1]
r = (curve.mul(private_b, c0[0]), curve.mul(private_b,c0[1]))

d = (curve.sub(c1[0], r[0]), curve.sub(c1[1], r[1]))
print(d)

# from __future__ import annotations
import math
import typing


def lcm(a: int, b: int) -> int:
    return a // math.gcd(a, b) * b


Fraction = typing.TypeVar("Fraction")


class Fraction:
    upper: int
    lower: int

    def __init__(self, upper: int, lower: int) -> None:
        self.upper = upper
        self.lower = lower

    def normalize(self) -> None:
        g = math.gcd(self.upper, self.lower)
        self.upper //= g
        self.lower //= g
        if self.lower < 0:
            self.lower *= -1
            self.upper *= -1

    def __add__(self, rhs: Fraction) -> Fraction:
        l = lcm(self.lower, rhs.lower)
        a, b = l // self.lower, l // rhs.lower
        return Fraction(self.upper * a + rhs.upper * b, l)

    def __neg__(self) -> Fraction:
        return Fraction(-self.upper, self.lower)

    def __sub__(self, rhs: Fraction) -> Fraction:
        return self + -rhs

    def __mul__(self, rhs: Fraction) -> Fraction:
        return Fraction(self.upper * rhs.upper, self.lower * rhs.lower)

    def __pow__(self, n: int) -> Fraction:
        if n == 0:
            return Fraction(1, 1)
        x = self ** (n >> 1)
        x = x * x
        if n & 1:
            x *= self
        return x

    def __repr__(self) -> str:
        return f"{self.upper}/{self.lower}"

    def floor(self) -> int:
        self.normalize()
        return self.upper // self.lower

    def ceil(self) -> int:
        floor = self.floor()
        if floor * self.lower == self.upper:
            return floor
        else:
            return floor + 1

    def __le__(self, rhs: Fraction) -> bool:
        res = self - rhs
        res.normalize()
        return res.upper <= 0

    def __eq__(self, rhs: Fraction) -> bool:
        return (self - rhs).upper == 0


def to_fraction(number: str) -> Fraction:
    parts = number.split(".")
    if len(parts) == 1:
        return Fraction(int(parts[0]), 1)
    assert len(parts) == 2
    p = 10 ** len(parts[1])
    return Fraction(int(parts[0]) * p + int(parts[1]), p)


def main() -> None:
    # to avoid errors,
    # denote all floating points numbers as fraction.
    # 1.11 -> 111 / 100
    # instead of computing dist, calculate dist^2
    # fix x and count up y.
    # the range of x is enough small.
    # (x - cx)^2 + (y - cy)^2 <= r^2
    # also, we neede to express integer as fraction
    # 100 -> 100 / 1
    # 10^5^2 * 10^4^2 = 10^18
    # lcm for addition and subtraction
    ...

    cx, cy, r = map(to_fraction, input().split())
    # print(cx, cy, r)

    # if x is fixed, solve (y - cy)^2 <= V
    # where V = r^2 - (x - cx)^2
    # if V < 0, then 0
    # we cannot use sqrt, so binary search min y and max y

    y0, y1 = cy.floor(), cy.ceil()
    x0, x1 = cx.floor(), cx.ceil()
    r2 = r * r

    def count_up_y(x: int) -> int:
        x_d = Fraction(x, 1) - cx
        rhs = r2 - x_d * x_d
        rhs.normalize()
        if rhs.upper < 0:
            return 0

        def search_max() -> int:
            lo, hi = y0, y1 + 10**5 + 1
            while hi - lo > 1:
                y = (lo + hi) >> 1
                y_d = Fraction(y, 1) - cy
                lhs = y_d * y_d
                lhs.normalize()
                if lhs <= rhs:
                    lo = y
                else:
                    hi = y
            return lo

        def search_min() -> int:
            hi, lo = y1, y0 - 10**5 - 1
            while hi - lo > 1:
                y = (lo + hi) >> 1
                y_d = Fraction(y, 1) - cy
                lhs = y_d * y_d
                lhs.normalize()
                if lhs <= rhs:
                    hi = y
                else:
                    lo = y
            return hi

        y_max = search_max()
        y_min = search_min()
        # print(rhs)
        # print(y_max, y_min, x)
        return y_max - y_min + 1

    # print(x0, x1, y0, y1)
    print(sum(count_up_y(x) for x in range(x0 - 10**5, x1 + 10**5 + 1)))


if __name__ == "__main__":
    main()

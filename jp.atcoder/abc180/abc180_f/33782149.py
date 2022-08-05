import typing
import abc

# mypy: ignore-errors
Modint = typing.TypeVar("Modint")
Intlike = typing.Union[Modint, int]


class Modint(abc.ABC):
    mod: typing.ClassVar[int]
    value: int

    def __init__(self, value: int) -> None:
        self.value = value % self.mod

    @classmethod
    def new(cls, x: Intlike) -> Modint:
        if type(x) != int:
            return typing.cast(Modint, x)
        else:
            return cls(typing.cast(int, x))

    def __repr__(self) -> str:
        return f"{self.value}"

    def clone(self) -> Modint:
        return self.new(self.value)

    def __add__(self, rhs: Intlike) -> Modint:
        return self.new(self.value + self.new(rhs).value)

    def __neg__(self) -> Modint:
        return self.new(-self.value)

    def __mul__(self, rhs: Intlike) -> Modint:
        return self.new(self.value * self.new(rhs).value)

    def inv(self) -> Modint:
        return self ** (self.mod - 2)
        # return self**-1  # RE in pypy

    def __sub__(self, rhs: Intlike) -> Modint:
        return self + -self.new(rhs)

    def __truediv__(self, rhs: Intlike) -> Modint:
        return self * self.new(rhs).inv()

    def __iadd__(self, rhs: Intlike) -> Modint:
        return self + self.new(rhs)

    def __isub__(self, rhs: Intlike) -> Modint:
        return self - self.new(rhs)

    def __imul__(self, rhs: Intlike) -> Modint:
        return self * self.new(rhs)

    def __itruediv__(self, rhs: Intlike) -> Modint:
        return self / self.new(rhs)

    def __radd__(self, lhs: int) -> int:
        return (self.new(lhs) + self).value

    def __rsub__(self, lhs: int) -> int:
        return (self.new(lhs) - self).value

    def __rmul__(self, lhs: int) -> int:
        return (self.new(lhs) * self).value

    def __rtruediv__(self, lhs: int) -> int:
        return (self.new(lhs) / self).value

    def __pow__(self, n: int) -> Modint:
        return self.new(pow(self.value, n, self.mod))

    def __ipow__(self, n: int) -> Modint:
        return self**n

    def __eq__(self, rhs: object) -> bool:
        if not isinstance(rhs, Modint):
            raise NotImplementedError
        return self.value == rhs.value


def define_modint(p: int) -> typing.Type[Modint]:
    class Mint(Modint):
        mod = p

    return Mint


T = typing.TypeVar("T")


def cumprod(a: typing.List[T]) -> typing.List[T]:
    n = len(a)
    for i in range(n - 1):
        a[i + 1] *= a[i]
    return a


def factorial(C: T, size: int) -> typing.List[T]:
    a = [C(i) for i in range(size)]
    a[0] = C(1)
    return cumprod(a)


def inverse_factorial(C: T, size: int) -> typing.List[T]:
    a = [C(i) for i in range(size, 0, -1)]
    a[0] = C(1) / factorial(C, size)[-1]
    return cumprod(a)[::-1]


class FactorialTablesFrequentOps(typing.Generic[T]):
    C: typing.ClassVar[typing.Type[T]]
    fact: typing.List[T]
    ifact: typing.List[T]

    def __init__(self, C: T, size: int) -> None:
        self.fact = factorial(C, size)
        self.ifact = inverse_factorial(C, size)

    def p(self, n: int, k: int) -> T:
        if k < 0 or n < k:
            return self.C(0)
        return self.fact[n] * self.ifact[n - k]

    def c(self, n: int, k: int) -> T:
        return self.p(n, k) * self.ifact[k]

    def h(self, n: int, k: int) -> T:
        return self.c(n - 1 + k, k)

    def inv(self, n: int) -> T:
        return self.fact[n - 1] * self.ifact[n]

    def inv_p(self, n: int, k: int) -> T:
        assert 0 <= k <= n
        return self.ifact[n] * self.fact[n - k]

    def inv_c(self, n: int, k: int) -> T:
        return self.inv_p(n, k) * self.fact[k]


def main() -> None:
    Mint = define_modint(1_000_000_007)
    size = 1 << 10
    f = FactorialTablesFrequentOps(Mint, size)
    n, m, l = map(int, input().split())
    path = [Mint(1)] * size
    path[0] = Mint(0)
    for i in range(3, size):
        path[i] = path[i - 1] * Mint(i)
    cycle = [Mint(0)] + path

    def g(l: int) -> Mint:
        dp = [[Mint(0)] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = Mint(1)
        for i in range(n):
            for j in range(m + 1):
                for k in range(1, l + 1):
                    if i + k > n:
                        break
                    x = dp[i][j] * f.c(n - i - 1, k - 1)
                    if j + k <= m:
                        dp[i + k][j + k] += x * cycle[k]
                    if j + k - 1 <= m:
                        dp[i + k][j + k - 1] += x * path[k]
        return dp[-1][-1]

    print(g(l) - g(l - 1))


if __name__ == "__main__":
    main()

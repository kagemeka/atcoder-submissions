# / mypy: ignore-errors
import typing


T = typing.TypeVar("T")


def power_recurse(
    op: typing.Callable[[T, T], T],
    e: typing.Optional[typing.Callable[[], T]] = None,
    inv: typing.Optional[typing.Callable[[T], T]] = None,
) -> typing.Callable[[T, int], T]:
    def f(x: T, n: int) -> T:
        if n == 0:
            assert e is not None
            return e()
        if n < 0:
            assert inv is not None
            return f(inv(x), -n)
        if n == 1:
            return x
        y = f(x, n >> 1)
        y = op(y, y)
        if n & 1:
            y = op(y, x)
        return y

    return f


def power(
    op: typing.Callable[[T, T], T],
    e: typing.Optional[typing.Callable[[], T]] = None,
    inv: typing.Optional[typing.Callable[[T], T]] = None,
) -> typing.Callable[[T, int], T]:
    def f(x: T, n: int) -> T:
        if n == 0:
            assert e is not None
            return e()
        if n < 0:
            assert inv is not None
            x = inv(x)
            n = -n
        y = x
        n -= 1
        while n:
            if n & 1:
                y = op(y, x)
            x = op(x, x)
            n >>= 1
        return y

    return f


T = typing.TypeVar("T")
Mat = typing.List[typing.List[T]]
Op = typing.Callable[[T, T], T]


def matrix_dot(add: Op, mul: Op) -> typing.Callable[[Mat, Mat], Mat]:
    def f(a: Mat, b: Mat) -> Mat:
        c = [[None] * len(b[0]) for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    v = mul(a[i][k], b[k][j])
                    c[i][j] = v if c[i][j] is None else add(c[i][j], v)
        return c

    return f


def factorial_table(
    mul: typing.Callable[[int, int], int],
    size: int,
) -> typing.List[int]:
    import itertools

    a = list(range(size))
    a[0] = 1
    return list(itertools.accumulate(a, mul))


def inverse_factorial_table(
    mul: typing.Callable[[int, int], int],
    inv: typing.Callable[[int], int],
    size: int,
) -> typing.List[int]:
    import itertools

    a = list(range(1, size + 1))
    a[-1] = inv(factorial_table(mul, size)[-1])
    return list(itertools.accumulate(a[::-1], mul))[::-1]


def modular_factorial_table(mod: int, size: int) -> typing.List[int]:
    return factorial_table(lambda a, b: a * b % mod, size)


def modular_inverse_factorial_table(p: int, size: int) -> typing.List[int]:
    return inverse_factorial_table(
        lambda a, b: a * b % p,
        lambda a: pow(a, p - 2, p),
        size,
    )


def combination(
    mul: typing.Callable[[int, int], int],
    inv: typing.Callable[[int], int],
    size: int,
) -> typing.Callable[[int, int], int]:
    fact = factorial_table(mul, size)
    ifact = inverse_factorial_table(mul, inv, size)

    def f(n: int, k: int) -> int:
        if not 0 <= k <= n:
            return 0
        return mul(mul(fact[n], ifact[n - k]), ifact[k])

    return f


def modular_combination(p: int, size: int) -> typing.Callable[[int, int], int]:
    return combination(
        lambda a, b: a * b % p,
        lambda a: pow(a, p - 2, p),
        size,
    )


def main() -> None:
    MOD = 998_244_353

    def add(a: int, b: int) -> int:
        return (a + b) % MOD

    def mul(a: int, b: int) -> int:
        return a * b % MOD

    dot = matrix_dot(add, mul)
    f = power(dot)

    n, d = map(int, input().split())

    choose = modular_combination(MOD, 1 << 15)

    def count_up(k: int) -> int:
        a = [
            [choose(d - 1, k), choose(d - 1, k - 1)],
            [choose(d - 1, k - 1), choose(d - 1, k - 2)],
        ]
        a = f(a, n)
        return a[0][0] + a[1][1] % MOD

    print(sum(count_up(i) for i in range(d + 2)) % MOD)


main()

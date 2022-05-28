import typing
import math


def f(n: int) -> int:
    return (1 + n) * n // 2


def main() -> None:
    n, a, b = map(int, input().split())

    l = a // math.gcd(a, b) * b

    def s(x: int) -> int:
        q = n // x
        return f(q) * x

    cnt = s(1) - (s(a) + s(b) - s(l))
    print(cnt)


if __name__ == "__main__":
    main()

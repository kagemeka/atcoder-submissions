# O(\sqrt{N})
# references
# - https://maspypy.com/atcoder-%e5%8f%82%e5%8a%a0%e6%84%9f%e6%83%b3-2020-06-27abc-172#toc4
import typing


def main() -> typing.NoReturn:
    n = int(input())

    # \sum_{ab \le n} ab
    # = \sum_{a=1}^{\lfloor{\sqrt{n}}\rfloor}{a^2 + 2a\sum_{ab \le n \land a \lt b} b}
    # a^2 + 2a\sum_{ab \le n \land a \lt b} b = a^2 + 2a(a + 1 + n // a) * (n // a - a) // 2
    # = a^2 + a(a + 1 + n // a) * (n // a - a)
    s = 0
    for i in range(1, n + 1):
        if i * i > n: break
        s += i * i + i * (i + 1 + n // i) * (n // i - i)
    print(s)

main()

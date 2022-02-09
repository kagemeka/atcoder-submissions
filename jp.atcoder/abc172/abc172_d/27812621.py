# fast zeta transform
import typing


def main() -> typing.NoReturn:
    n = int(input())

    s = 0
    for i in range(1, n + 1):
        if i * i > n: break
        s += i * i + 2 * i * (i + 1 + n // i) * (n // i - i) // 2
    print(s)

main()

import typing


def main() -> typing.NoReturn:
    a, b, n = map(int, input().split())
    ans = a * n // b - a * (n // b)
    if n >= b:
        m = n // b * b - 1
        ans = max(ans, a * m // b - a * (m // b))
    print(ans)

main()

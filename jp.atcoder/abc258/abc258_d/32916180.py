# / mypy: ignore-errors
import typing


def main() -> None:
    n, x = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    s = [0] * (n + 1)
    for i in range(n):
        a, b = ab[i]
        s[i + 1] = s[i] + a + b

    inf = 1 << 60
    mn = inf
    for i in range(n):
        if x <= i:
            break
        a, b = ab[i]
        mn = min(mn, s[i] + a + max(0, (x - i) * b))
    print(mn)


main()

# / mypy: ignore-errors
import typing


def main() -> None:
    n, q = map(int, input().split())
    s = input()

    res = []
    i = 0
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            i = (i - x) % n
        else:
            x -= 1
            res.append(s[(i + x) % n])
    print(*res, sep="\n")


main()

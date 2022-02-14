import typing
import sys

sys.setrecursionlimit(1 << 20)


def main() -> None:
    x = int(input())
    res = []

    def split(x: int) -> None:
        if x <= 4:
            res.append(x)
            return
        x, y = x // 2, (x + 1) // 2
        split(x)
        split(y)

    split(x)
    p = 1
    MOD = 998_244_353
    for x in res:
        p *= x
        p %= MOD
    print(p)


if __name__ == "__main__":
    main()

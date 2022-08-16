# mypy: ignore-errors

import sys


read = sys.stdin.read
readline = sys.stdin.readline


def main() -> None:
    sx, sy, tx, ty = map(int, readline().split())
    x = tx - sx
    y = ty - sy
    res = ""
    res += "u" * y
    res += "r" * (x + 1)
    res += "d" * (y + 1)
    res += "l" * (x + 1)
    res += "u"
    res += "l"
    res += "u" * (y + 1)
    res += "r" * (x + 1)
    res += "d" * (y + 1)
    res += "l" * x
    print(res.upper())


if __name__ == "__main__":
    main()

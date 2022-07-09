# mypy: ignore-errors

import math


def main() -> None:
    a, b, d = map(int, input().split())
    t = math.tau * d / 360
    x = math.cos(t) * a - math.sin(t) * b
    y = math.sin(t) * a + math.cos(t) * b
    print(x, y)


main()

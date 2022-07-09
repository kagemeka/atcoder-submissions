# mypy: ignore-errors

import math


def main() -> None:
    n, m, x, t, d = map(int, input().split())

    t0 = t - x * d

    print(t0 + min(m, x) * d)


main()

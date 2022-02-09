import typing

import math

def dist(x0: int, y0: int, x1: int, y1: int) -> float:
    return math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)


def main() -> None:
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]

    mx = 0
    for i in range(n):
        for j in range(n):
            x0, y0 = xy[i]
            x1, y1 = xy[j]
            mx = max(mx, dist(x0, y0, x1, y1))
    print(mx)


main()

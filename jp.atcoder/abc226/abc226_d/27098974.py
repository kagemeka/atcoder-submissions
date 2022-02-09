import typing
import math


def main() -> typing.NoReturn:
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]

    s = set()
    for i in range(n):
        for j in range(n):
            if i == j: continue
            dx = xy[j][0] - xy[i][0]
            dy = xy[j][1] - xy[i][1]
            g = math.gcd(dx, dy)
            s.add((dx // g, dy // g))
    print(len(s))

main()

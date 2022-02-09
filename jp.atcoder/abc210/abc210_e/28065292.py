import typing
import math

def main() -> typing.NoReturn:
    n, m = map(int, input().split())

    ac = [tuple(map(int, input().split())) for _ in range(m)]
    ac.sort(key=lambda x: x[1])
    g = n
    cost = 0
    for a, c in ac:
        g2 = math.gcd(g, a)
        if g2 == g: continue
        cost += (g - g2) * c
        g = g2
    if g != 1:
        print(-1)
    else:
        print(cost)

main()

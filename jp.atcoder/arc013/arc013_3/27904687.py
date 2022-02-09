import typing


def main() -> typing.NoReturn:
    n = int(input())
    g0 = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        m = int(input())
        xyz = [tuple(map(int, input().split())) for _ in range(m)]
        x, y, z = zip(*xyz)
        g = 0
        g ^= a - max(x) - 1
        g ^= min(x)
        g ^= b - max(y) - 1
        g ^= min(y)
        g ^= c - max(z) - 1
        g ^= min(z)
        g0 ^= g
    print('LOSE' if g0 == 0 else 'WIN')

main()

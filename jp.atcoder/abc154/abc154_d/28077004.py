import typing


def main() -> typing.NoReturn:
    # E[aX + bY] = aE[X] + bE[Y]
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ex = [(1 + x) / 2 for x in p]
    s = sum(ex[:k])
    mx = s
    for i in range(k, n):
        s = s - ex[i - k] + ex[i]
        mx = max(mx, s)

    print(mx)

main()

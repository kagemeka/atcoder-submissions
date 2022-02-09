import typing


def main() -> typing.NoReturn:
    n = int(input())
    t = [int(input()) for _ in range(n)]

    st = sum(t)
    mn = 1 << 60
    for s in range(1 << n):
        tot = 0
        for i in range(n):
            if ~s >> i & 1: continue
            tot += t[i]
        mn = min(mn, max(tot, st - tot))

    print(mn)

main()

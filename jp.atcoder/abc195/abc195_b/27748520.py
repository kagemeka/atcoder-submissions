import typing


def main() -> typing.NoReturn:
    a, b, w = map(int, input().split())
    w *= 1000
    inf = 1 << 60
    mn, mx = inf, 0
    for cnt in range(1, 1 << 20):
        if not(a * cnt <= w <= b * cnt): continue
        mn = min(mn, cnt)
        mx = max(mx, cnt)
    if mx == 0:
        print('UNSATISFIABLE')
    else:
        print(mn, mx)


main()

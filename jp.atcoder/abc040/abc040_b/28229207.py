import typing


def main() -> typing.NoReturn:
    n = int(input())

    # n = h * w + r
    # minimize |h - w| + r

    # inf = 1 << 60
    mn = n # h = 0
    for h in range(1, n + 1):
        if h * h > n: break
        w = n // h

        mn = min(mn, w - h + n - w * h)
    print(mn)

main()

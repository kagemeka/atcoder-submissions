import typing


def main() -> typing.NoReturn:
    h = w = 1500
    n = 100
    res = [None] * n
    lo, hi = 0, n
    x0 = 0
    while lo < hi:
        y_list = []
        y = 0
        while lo < hi and y + 2 * hi <= h:
            res[hi - 1] = (x0 + hi, y + hi)
            y_list.append(y + hi)
            y += 2 * hi
            hi -= 1

        for y in y_list:
            if lo >= hi: break
            res[lo] = (x0 + 2 * (n + 1) - lo - 1, y)
            lo += 1
        x0 += n + 1
    print(res)
    for x, y in res:
        print(x, y)


main()

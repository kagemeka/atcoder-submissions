import typing


def main() -> typing.NoReturn:
    r, x, y = map(int, input().split())
    d2 = x ** 2 + y ** 2

    def binary_search() -> int:
        lo, hi = 0, 1 << 20
        while hi - lo > 1:
            cnt = (lo + hi) // 2
            if cnt ** 2 * r ** 2 >= d2:
                hi = cnt
            else:
                lo = cnt
        return hi

    print(binary_search())


main()

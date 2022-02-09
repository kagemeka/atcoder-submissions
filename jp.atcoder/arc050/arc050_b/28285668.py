import typing



def main() -> typing.NoReturn:
    # ternary search ?
    r, b = map(int, input().split())
    x, y = map(int, input().split())


    def count(c: int) -> int:
        assert 0 <= c <= min(r // x, b)
        return c + min(r - x * c, (b - c) // y)

    def ternary_search() -> int:
        # return the number of red bouquet
        lo, hi = 0, min(r // x, b)

        while hi - lo > 1:
            c0 = (2 * lo + hi + 3 - 1) // 3
            c1 = (lo + 2 * hi) // 3
            # print(lo, c0, c1, hi)
            assert c0 <= c1
            if count(c0) < count(c1):
                lo = c0
            else:
                hi = c1
        # print(lo, hi)
        # print(count(lo), count(hi))
        return lo if count(lo) >= count(hi) else hi

    c = ternary_search()
    print(count(ternary_search()))


main()

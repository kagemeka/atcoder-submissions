import typing
import sys



def main() -> typing.NoReturn:
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())


    lo_0 = max(1 - a, 1 - b)
    hi_0 = min(n - a, n - b)
    lo_1 = max(1 - a, b - n)
    hi_1 = min(n - a, b - 1)

    def is_black(i: int, j: int) -> bool:
        ok = lo_0 <= i - a <= hi_0 and lo_0 <= j - b <= hi_0 and i - a == j - b
        ok |= lo_1 <= i - a <= hi_1 and lo_1 <= -(j - b) <= hi_1 and i - a == -(j - b)
        return ok


    for i in range(p, q + 1):
        row = ''.join(('#' if is_black(i, j) else '.' for j in range(r, s + 1)))
        # for j in range(r, s + 1):
        print(row)


main()

import typing
import sys
import bisect


def main() -> typing.NoReturn:
    n = int(input())

    # v = n
    i = 1
    def binary_search(i: int) -> int:
        lo = i
        hi = 1 << 60
        while hi - lo > 1:
            j = (lo + hi) // 2
            if n // j < n // i:
                hi = j
            else:
                lo = j
        return hi

    s = 0
    while i <= n:
        j = binary_search(i)
        s += n // i * (j - i)
        i = j
    print(s)




main()

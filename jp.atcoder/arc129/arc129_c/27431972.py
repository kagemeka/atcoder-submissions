import typing
import bisect


def main() -> typing.NoReturn:
    n = int(input())
    a = [(1 << i) - 1 for i in range(1, 30)]
    s = []
    while n:
        i = bisect.bisect_right(a, n)
        n -= a[i - 1]
        s.append('7' * i)
    print('1'.join(s))


main()

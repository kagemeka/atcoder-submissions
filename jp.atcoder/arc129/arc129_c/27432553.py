import typing
import bisect


def main() -> typing.NoReturn:
    n = int(input())
    a = [(1 << i) - 1 for i in range(1, 30)]
    s = []
    n0 = n
    tot = 0
    while n:
        i = bisect.bisect_right(a, n)
        assert i < 30
        n -= a[i - 1]
        tot += a[i - 1]
        s.append('7' * i)
    assert tot == n0
    print('1'.join(s))


main()

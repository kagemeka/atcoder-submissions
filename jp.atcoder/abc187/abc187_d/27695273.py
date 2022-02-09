import typing
import sys
import functools

def main() -> typing.NoReturn:
    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]

    def cmp(x: typing.Tuple[int, int], y: typing.Tuple[int, int]) -> bool:
        return 2 * (x[0] - y[0]) + x[1] - y[1]


    ab.sort(key=functools.cmp_to_key(cmp))
    s = sum(a for a, _ in ab)
    t = 0
    for i in range(n):
        a, b = ab[-1 - i]
        t += a + b
        s -= a
        if t > s:
            print(i + 1)
            return


main()

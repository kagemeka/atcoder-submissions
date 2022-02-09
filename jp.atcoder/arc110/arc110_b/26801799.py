import typing
import sys
import numpy as np
import numba as nb


def main() -> typing.NoReturn:
    n = int(input())
    s = input()
    if n == 1:
        cnt = 10 ** 10 * (2 if s == '1' else 1)
        print(cnt)
        return

    if s[:2] == '11': pass
    elif s[:2] == '10':
        n += 1
        s = '1' + s
    elif s[:2] == '01':
        n += 2
        ss = '11' + s

    t = '110' * (1 << 17)
    if t[:n] != s:
        print(0)
        return
    print((10 ** 10 * 3 - n) // 3 + 1)


main()

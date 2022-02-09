import typing
import sys
import numpy as np
import numba as nb


@nb.njit(cache=True)
def solve() -> typing.NoReturn:
    ...


def main() -> typing.NoReturn:
    s = input()
    if s[-2:] == 'er':
        print('er')
    else:
        print('ist')


main()

import sys
import typing

import numba as nb
import numpy as np


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

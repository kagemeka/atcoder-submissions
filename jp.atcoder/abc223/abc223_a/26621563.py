import sys
import typing

import numba as nb
import numpy as np


def solve() -> typing.NoReturn:
    ...


def main() -> typing.NoReturn:
    x = int(input())
    ans = 'Yes' if x >= 100 and x % 100 == 0 else 'No'
    print(ans)


main()

import typing
import numpy as np
import sys
import itertools


def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    t = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, n)

    perms = itertools.permutations(range(1, n))
    perms = np.array([*perms])
    perms = np.pad(perms, ((0, 0), (1, 1)))
    d = np.sum(t[perms[:, :-1], perms[:, 1:]], axis=1)
    print(np.count_nonzero(d == k))

main()

import typing
import sys
# import numpy as np
# import numba as nb


# @nb.njit((nb.i8, nb.i8[:, :]), cache=True)
# def solve(n: int, ab:np.ndarray) -> typing.NoReturn:
def solve(n: int, g: typing.List[typing.Set[int]]) -> typing.NoReturn:
    a = []

    que = list(range(n))
    for i in que:
        if not len(g[i]):
            a.append(i)
            continue
        for j in g[i]:
            if not i in g[j]: continue
            print(-1)
            return
        g[i] = set()
        que.append(i)
    print(*[x + 1 for x in a])


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    g = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[b].add(a)
    solve(n, g)


main()

import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8, nb.i8[:]), cache=True)
def solve(n: int, q: np.ndarray) -> typing.NoReturn:
    parent = np.full(n, -1, np.int64)
    child = np.full(n, -1, np.int64)
    result = [[0] * 0] * 0
    while len(q) > 0:
        t = q[0]
        if t == 0:
            x, y = q[1:3]
            q = q[3:]
            parent[y] = x
            child[x] = y
        elif t == 1:
            x, y = q[1:3]
            q = q[3:]
            parent[y] = child[x] = -1
        elif t == 2:
            res = [0] * 0
            x = q[1]
            q = q[2:]
            st = [0] * 0
            y = x
            while y != -1:
                st.append(y)
                y = parent[y]
            while st:
                res.append(st.pop() + 1)
            y = x
            while child[y] != -1:
                y = child[y]
                res.append(y + 1)
            result.append(res)
    return result




def main() -> typing.NoReturn:
    n, q = map(int, input().split())
    q = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ) - 1
    res = solve(n, q)
    for x in res:
        print(len(x), *x)
    # print(res)


main()

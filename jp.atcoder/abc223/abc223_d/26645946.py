import typing
import sys
# import numpy as np
# import numba as nb
import heapq

# @nb.njit((nb.i8, nb.i8[:, :]), cache=True)
# def solve(n: int, ab:np.ndarray) -> typing.NoReturn:
def solve(n: int, g: typing.List[typing.Set[int]]) -> typing.NoReturn:

    for i in range(n):
        for j in g[i]:
            if not i in g[j]: continue
            print(-1)
            return

    # parent = list(range(n))
    # for i in range(n):
    #     for j in g[i]:
    #         parent[j] = i
    parents = [[] for _ in range(n)]
    for i in range(n):
        for j in g[i]:
            parents[j].append(i)
    a = []
    hq = []
    for i in range(n):
        if not parents[i]: heapq.heappush(hq, i)

    used = [False] * n
    while hq:
        i = heapq.heappop(hq)
        if used[i]: continue
        a.append(i)
        used[i] = True
        for j in g[i]:
            if used[j]: continue
            heapq.heappush(hq, j)
    print(*[x + 1 for x in a])


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    g = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].add(b)
    solve(n, g)
    # ab = np.array(



main()

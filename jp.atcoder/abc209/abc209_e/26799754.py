r"""Note.

shiritori
    - word -> edge
    - head, tail -> node

game theory
    - consider from terminal nodes.
    - backtrack.
"""

import typing
import sys
import string
import functools
sys.setrecursionlimit(1 << 20)


def main() -> typing.NoReturn:
    n = int(input())
    s = sys.stdin.read().split()
    alp = string.ascii_letters
    m = len(alp)
    to_int = dict(zip(alp, range(m)))
    head = [-1] * n
    tail = [-1] * n
    for i in range(n):
        w = s[i]
        v = 0
        d = 1
        for c in w[:3][::-1]:
            v += to_int[c] * d
            d *= m
        head[i] = v
        v = 0
        d = 1
        for c in w[-3:][::-1]:
            v += to_int[c] * d
            d *= m
        tail[i] = v

    to = [[] for _ in range(1 << 18)]
    deg = [0] * (1 << 18)
    for i in range(n):
        to[tail[i]].append(head[i])
        deg[head[i]] +=  1

    que = []
    res = [0] * (1 << 18)
    for i in range(1 << 18):
        if deg[i] > 0: continue
        res[i] = -1
        que.append(i)

    for v in que:
        if res[v] == -1:
            for u in to[v]:
                if res[u] != 0: continue
                res[u] = 1
                que.append(u)
        elif res[v] == 1:
            for u in to[v]:
                if res[u] != 0: continue
                deg[u] -= 1
                if deg[u] > 0: continue
                res[u] = -1
                que.append(u)
    for i in range(n):
        f = res[tail[i]]
        ans = 'Takahashi' if f == -1 else 'Draw' if f == 0 else 'Aoki'
        print(ans)


main()

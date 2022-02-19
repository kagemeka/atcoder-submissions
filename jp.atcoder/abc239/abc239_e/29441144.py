# from __future__ import annotations
import sys

sys.setrecursionlimit(1 << 20)


def main() -> None:
    n, q = map(int, input().split())
    values = list(map(int, input().split()))
    ab = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]
    g = [[] for _ in range(n)]
    for a, b in ab:
        g[a].append(b)
        g[b].append(a)

    vk = []
    for _ in range(q):
        v, k = map(int, input().split())
        v -= 1
        vk.append((v, k))

    cand = [[x] for x in values]

    def dfs(u: int, parent: int) -> None:
        for v in g[u]:
            if v == parent:
                continue
            dfs(v, u)
            cand[u] += cand[v]
        cand[u] = sorted(cand[u])[-20:]

    dfs(0, -1)
    for v, k in vk:
        print(cand[v][-k])


if __name__ == "__main__":
    main()

import typing
import sys
sys.setrecursionlimit(1 << 20)


def main() -> typing.NoReturn:
    n = int(input())
    # DP
    # first
    # second
    # subtree

    parent = [-1] + list(map(lambda x: int(x) - 1, input().split()))
    childs = [[] for _ in range(n)]
    for i in range(1, n):
        childs[parent[i]].append(i)
    que = []
    for i in range(n):
        if not childs[i]:
            que.append(i)

    size = [1] * n
    deg = [len(childs[i]) for i in range(n)]
    for u in que:
        p = parent[u]
        if p == -1: break
        size[p] += size[u]
        deg[p] -= 1
        if deg[p] == 0:
            que.append(p)

    def dfs(u: int) -> typing.Tuple[int, int]:
        # dfs on subtree
        # return first player's score and second player's score (optimal)
        first, second = 0, 1
        odd = []
        even = []
        for v in childs[u]:
            if size[v] & 1:
                odd.append(dfs(v))
            else:
                even.append(dfs(v))
        for f, s in even:
            if f > s or ~len(odd) & 1:
                first += f
                second += s
            else:
                first += s
                second += f
        odd.sort(key=lambda x: x[1] - x[0])
        for f, s in odd[::2]:
            first += f
            second += s
        for f, s in odd[1::2]:
            first += s
            second += f
        return first, second

    first, second = dfs(0)
    print(second)



main()

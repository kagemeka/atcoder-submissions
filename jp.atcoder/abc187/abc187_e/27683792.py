import typing
import sys
sys.setrecursionlimit(1 << 20)

def tree_bfs(
    g: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.Tuple[(typing.List[int], ) * 2]:
    n = len(g) + 1
    t = [[] for _ in range(n)]
    for u, v in g:
        t[u].append(v)
        t[v].append(u)
    parent = [-1] * n
    depth = [0] * n
    que = [root]
    for u in que:
        for v in t[u]:
            if v == parent[u]: continue
            parent[v] = u
            depth[v] = depth[u] + 1
            que.append(v)
    return parent, depth



def main() -> typing.NoReturn:
    n = int(input())
    ab = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]

    parent, depth = tree_bfs(ab, 0)
    v = [0] * n
    q = int(input())
    for _ in range(q):
        t, e, x = map(int, input().split())
        t -= 1
        a, b = ab[e - 1]
        if parent[a] == b:
            a, b = b, a
            t ^= 1
        if t == 1:
            v[b] += x
        else:
            v[0] += x
            v[b] -= x



    import functools
    @functools.lru_cache(maxsize=None)
    def dfs(u: int) -> int:
        if u == 0: return v[0]
        v[u] += dfs(parent[u])
        return v[u]

    for i in range(n):
        dfs(i)
    print(*v, sep='\n')

main()

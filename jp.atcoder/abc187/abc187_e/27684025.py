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



def euler_tour(
    g: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.Tuple[(typing.List[int], ) * 3]:
    n = len(g) + 1
    t = [[] for _ in range(n)]
    for u, v in g:
        t[u].append(v)
        t[v].append(u)
    parent = [-1] * n
    depth = [0] * n
    tour = []

    def dfs(u: int) -> typing.NoReturn:
        tour.append(u)
        for v in t[u]:
            if v == parent[u]: continue
            parent[v] = u
            depth[v] = depth[u] + 1
            dfs(v)
        tour.append(~u)

    dfs(root)
    return tour, parent, depth


def to_nodes(tour: typing.List[int], parent: typing.List[int]) -> typing.List[int]:
    return [u if u >= 0 else parent[~u] for u in tour[:-1]]



def main() -> typing.NoReturn:
    n = int(input())
    ab = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]

    tour, parent, _ = euler_tour(ab, 0)
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

    for u in tour:
        if u < 0 or parent[u] < 0: continue
        v[u] += v[parent[u]]

    print(*v, sep='\n')

main()

import typing

def tree_bfs(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.Tuple[typing.List[int], typing.List[int]]:
    n = len(tree_edges) + 1
    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u, v in tree_edges:
        graph[u].append(v)
        graph[v].append(u)
    parent = [-1] * n
    depth = [0] * n
    que = [root]
    for u in que:
        for v in graph[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            que.append(v)
    return parent, depth


def lca_binary_lifting(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.Callable[[int, int], int]:
    n = len(tree_edges) + 1
    parent, depth = tree_bfs(tree_edges, root)
    k = max(1, max(depth).bit_length())
    ancestor = [[n] * n for _ in range(k)]
    ancestor[0] = parent
    ancestor[0][root] = root
    for i in range(k - 1):
        for j in range(n):
            ancestor[i + 1][j] = ancestor[i][ancestor[i][j]]

    def get(u: int, v: int) -> int:
        if depth[u] > depth[v]:
            u, v = v, u
        d = depth[v] - depth[u]
        for i in range(d.bit_length()):
            if d >> i & 1:
                v = ancestor[i][v]
        if v == u:
            return u
        for a in ancestor[::-1]:
            nu, nv = a[u], a[v]
            if nu != nv:
                u, v = nu, nv
        return parent[u]

    return get


def lca_tarjan_offline(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
    query_pairs: typing.List[typing.Tuple[int, int]],
) -> typing.List[int]:
    n = len(tree_edges) + 1
    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u, v in tree_edges:
        graph[u].append(v)
        graph[v].append(u)
    queries: typing.List[typing.List[typing.Tuple[int, int]]] = [
        [] for _ in range(n)
    ]
    for i, (u, v) in enumerate(query_pairs):
        queries[u].append((v, i))
        queries[v].append((u, i))
    visited = [False] * n
    uf = UnionFind(n)
    ancestor = [n] * n
    lca = [n] * len(query_pairs)

    def dfs(u: int) -> None:
        visited[u] = True
        ancestor[u] = u
        for v in graph[u]:
            if visited[v]:
                continue
            dfs(v)
            uf.unite(u, v)
            ancestor[uf.find(u)] = u

        for v, query_id in queries[u]:
            if visited[v]:
                lca[query_id] = ancestor[uf.find(v)]

    dfs(root)
    return lca

class UnionFind():
    def __init__(self, n: int) -> None:
        self.__data = [-1] * n

    def __len__(self) -> int:
        return len(self.__data)

    def find(self, u: int) -> int:
        d = self.__data
        if d[u] < 0:
            return u
        d[u] = self.find(d[u])
        return d[u]

    def unite(self, u: int, v: int) -> None:
        u, v = self.find(u), self.find(v)
        if u == v:
            return
        d = self.__data
        if d[u] > d[v]:
            u, v = v, u
        d[u] += d[v]
        d[v] = u

    def size(self, u: int) -> int:
        return -self.__data[self.find(u)]


def main() -> None:
    n = int(input())
    edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]
    q = int(input())
    res = []

    _, depth = tree_bfs(edges, 0)
    # get = lca_binary_lifting(edges, 0)

    # def dist(u: int, v: int) -> int:
    #     return depth[u] + depth[v] - 2 * depth[get(u, v)]

    # for _ in range(q):
    #     u, v = map(int, input().split())
    #     u -= 1
    #     v -= 1
    #     res.append(dist(u, v) + 1)

    queries = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(q)]
    lca = lca_tarjan_offline(edges, 0, queries)
    for i in range(q):
        u, v = queries[i]
        res.append(depth[u] + depth[v] - 2 * depth[lca[i]] + 1)


    print(*res, sep='\n')

main()

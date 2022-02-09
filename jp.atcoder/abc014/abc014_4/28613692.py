import typing
import sys
# import dataclasses
sys.setrecursionlimit(1 << 20)


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


def lca_euler_tour_rmq(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.Callable[[int, int], int]:
    # sparse table
    # segment tree
    # sqrt decomposition
    # here, using sparse table
    tour = euler_tour(tree_edges, root)
    depth = compute_depth(tour)
    tour = to_nodes(tour)
    first_idx = compute_first_index(tour)
    semigroup = Semigroup[typing.Tuple[int, int]](op=min)
    get_min = sparse_table(semigroup, [(depth[i], i) for i in tour])

    def get_lca(u: int, v: int) -> int:
        left, right = first_idx[u], first_idx[v]
        if left > right:
            left, right = right, left
        return get_min(left, right + 1)[1]

    return get_lca


S = typing.TypeVar("S")


# @dataclasses.dataclass
class Semigroup(typing.Generic[S]):
    op: typing.Callable[[S, S], S]

    def __init__(self, op) -> None:
        self.op = op


def bit_length_table(n: int) -> typing.List[int]:
    """Bit length table.

    Args:
        n (int): an unsigned integer.

    Returns:
        list[int]: bit length table.

    Complexity:
        time: O(N)
        space: O(N)
    """
    length = [0] * n
    for i in range(1, n):
        length[i] = length[i >> 1] + 1
    return length


def sparse_table(
    semigroup: Semigroup[S],
    arr: typing.List[S],
) -> typing.Callable[[int, int], S]:
    # [left, right)
    n = len(arr)
    assert n > 0
    bit_length = bit_length_table(n + 1)
    k = max(1, bit_length[n - 1])
    data = [arr.copy()]
    for i in range(k - 1):
        data.append(data[i].copy())
        for j in range(n - (1 << i)):
            data[i + 1][j] = semigroup.op(data[i][j], data[i][j + (1 << i)])

    def get(left: int, right: int) -> S:
        assert 0 <= left < right <= n
        if right - left == 1:
            return data[0][left]
        k = bit_length[right - 1 - left] - 1
        return semigroup.op(data[k][left], data[k][right - (1 << k)])

    return get


def euler_tour(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.List[int]:
    """Euler Tour.

    Args:
        tree_edges (typing.List[typing.Tuple[int, int]]):
            undirected graph edges.
        root (int): tour root node.

    Returns:
        typing.List[int]: the result array represent the tour on edges.

    Examples:
        >>> edges = [(0, 1), (0, 3), (1, 4), (1, 2)]
        >>> euler_tour(edges, 0)
        [0, 1, 4, -5, 2, -3, -2, 3, -4, -1]
    """
    n = len(tree_edges) + 1
    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u, v in tree_edges:
        graph[u].append(v)
        graph[v].append(u)
    parent: typing.List[typing.Optional[int]] = [None] * n
    tour = [-1] * (n << 1)

    st = [root]
    for i in range(n << 1):
        u = st.pop()
        tour[i] = u
        if u < 0:
            continue
        st.append(~u)
        for v in graph[u][::-1]:
            if v == parent[u]:
                continue
            parent[v] = u
            st.append(v)
    return tour


def to_nodes(tour_edges: typing.List[int]) -> typing.List[int]:
    """Convert Euler-tour-on-edges to Euler-tour-on-nodes.

    Args:
        tour_edges (typing.List[int]): euler tour on edges.

    Returns:
        typing.List[int]: euler tour on nodes.

    Examples:
        >>> tour_edges = [0, 1, 4, -5, 2, -3, -2, 3, -4, -1]
        >>> to_nodes(tour_edges)
        [0, 1, 4, 1, 2, 1, 0, 3, 0]
    """
    parent = compute_parent(tour_edges)
    tour_nodes: typing.List[int] = []
    for u in tour_edges[:-1]:
        if u >= 0:
            tour_nodes.append(u)
        else:
            p = parent[~u]
            assert p is not None
            tour_nodes.append(p)
    return tour_nodes


def compute_parent(
    tour_edges: typing.List[int],
) -> typing.List[typing.Optional[int]]:
    """Compute parent from Euler-tour-on-edges.

    Args:
        tour_edges (typing.List[int]): euler tour on edges.

    Returns:
        typing.List[typing.Optional[int]]:
            parent list.
            the tour root's parent is None.

    Examples:
        >>> tour_edges = [0, 1, 4, -5, 2, -3, -2, 3, -4, -1]
        >>> compute_parent(tour_edges)
        [None, 0, 1, 0, 1]
    """
    n = len(tour_edges) >> 1
    parent: typing.List[typing.Optional[int]] = [None] * n
    st = [tour_edges[0]]
    for u in tour_edges[1:]:
        if u < 0:
            st.pop()
            continue
        parent[u] = st[-1]
        st.append(u)

    return parent


def compute_depth(tour_edges: typing.List[int]) -> typing.List[int]:
    """Compute depth from Euler-tour-on-edges.

    Args:
        tour_edges (typing.List[int]): euler tour on edges.

    Returns:
        typing.List[int]: depth list.

    Examples:
        >>> tour_edges = [0, 1, 4, -5, 2, -3, -2, 3, -4, -1]
        >>> compute_depth(tour_edges)
        [0, 1, 2, 1, 2]

    """
    n = len(tour_edges) >> 1
    parent = compute_parent(tour_edges)
    depth = [0] * n
    for u in tour_edges[1:]:
        if u < 0:
            continue
        p = parent[u]
        assert p is not None
        depth[u] = depth[p] + 1
    return depth


def compute_first_index(tour_nodes: typing.List[int]) -> typing.List[int]:
    """Compute first index in euler tour from euler tour on nodes.

    Args:
        tour_nodes (typing.List[int]): euler tour on nodes.

    Returns:
        typing.List[int]: first indices.

    Examples:
        >>> tour_nodes = [0, 1, 4, 1, 2, 1, 0, 3, 0]
        >>> compute_first_index(tour_nodes)
        [0, 1, 4, 7, 2]
    """
    n = len(tour_nodes) + 1 >> 1
    first_idx = [-1] * n
    for i, u in enumerate(tour_nodes):
        if first_idx[u] == -1:
            first_idx[u] = i
    return first_idx


def hl_decompose(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.List[int]:
    # range query: O(\log^2{N})
    # return labels
    n = len(tree_edges) + 1
    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u, v in tree_edges:
        graph[u].append(v)
        graph[v].append(u)
    size = [1] * n
    labels = [-1] * n
    label = 0

    def dfs(u: int, parent: int) -> int:
        nonlocal label
        heavy_node, max_size = None, 0
        for v in graph[u]:
            if v == parent:
                continue
            size[u] += dfs(v, u)
            if size[v] > max_size:
                heavy_node, max_size = v, size[v]
        if heavy_node is None:
            labels[u] = label
            label += 1
        else:
            labels[u] = labels[heavy_node]
        return size[u]

    dfs(root, -1)
    return labels


def compute_roots(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
    labels: typing.List[int],
) -> typing.List[int]:
    n = len(tree_edges) + 1
    k = max(labels) + 1
    roots = [-1] * k
    min_depth = [n] * k
    _, depth = tree_bfs(tree_edges, root)
    for i, label in enumerate(labels):
        if depth[i] < min_depth[label]:
            min_depth[label] = depth[i]
            roots[label] = i
    return roots


def lca_hld(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.Callable[[int, int], int]:
    parent, depth = tree_bfs(tree_edges, root)
    labels = hl_decompose(tree_edges, root)
    roots = compute_roots(tree_edges, root, labels)
    roots = [roots[label] for label in labels]

    def get_lca(u: int, v: int) -> int:
        while True:
            if roots[u] == roots[v]:
                return u if depth[u] <= depth[v] else v
            if depth[roots[u]] > depth[roots[v]]:
                u, v = v, u
            v = parent[roots[v]]
            assert v != -1

    return get_lca


def main() -> None:
    n = int(input())
    edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]
    q = int(input())
    res = []

    _, depth = tree_bfs(edges, 0)
    # get = lca_binary_lifting(edges, 0)
    # get = lca_euler_tour_rmq(edges, 0)
    get = lca_hld(edges, 0)

    def dist(u: int, v: int) -> int:
        return depth[u] + depth[v] - 2 * depth[get(u, v)]

    for _ in range(q):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        res.append(dist(u, v) + 1)

    # queries = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(q)]
    # lca = lca_tarjan_offline(edges, 0, queries)
    # for i in range(q):
    #     u, v = queries[i]
    #     res.append(depth[u] + depth[v] - 2 * depth[lca[i]] + 1)


    print(*res, sep='\n')

main()

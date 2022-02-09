import typing
import dataclasses

S = typing.TypeVar("S")


@dataclasses.dataclass
class Monoid(typing.Generic[S]):
    op: typing.Callable[[S, S], S]
    e: typing.Callable[[], S]


def query_on_path_binary_lifting(
    monoid: Monoid[S],
    tree_edges: typing.List[typing.Tuple[int, int, S]],
) -> typing.Callable[[int, int], S]:
    # moniod operation must be commutative
    root = 0
    n = len(tree_edges) + 1
    graph: typing.List[typing.List[typing.Tuple[int, S]]] = [
        [] for _ in range(n)
    ]
    for u, v, value in tree_edges:
        graph[u].append((v, value))
        graph[v].append((u, value))
    que = [root]
    parent = [-1] * n
    depth = [0] * n
    value_to_parent = [monoid.e() for _ in range(n)]
    for u in que:
        for v, value in graph[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            value_to_parent[v] = value
            que.append(v)

    k = max(1, max(depth).bit_length())
    ancestor = [[n] * n for _ in range(k)]
    ancestor[0] = parent
    ancestor[0][root] = root
    value_to_ancestor = [value_to_parent]
    for i in range(k - 1):
        value_to_ancestor.append(value_to_ancestor[-1].copy())
        for j in range(n):
            ancestor[i + 1][j] = ancestor[i][ancestor[i][j]]
            value_to_ancestor[i + 1][j] = monoid.op(
                value_to_ancestor[i][j],
                value_to_ancestor[i][ancestor[i][j]],
            )

    def get_value(u: int, v: int) -> S:
        value = monoid.e()
        if depth[u] > depth[v]:
            u, v = v, u
        d = depth[v] - depth[u]
        for i in range(d.bit_length()):
            if d >> i & 1:
                value = monoid.op(value, value_to_ancestor[i][v])
                v = ancestor[i][v]
        if v == u:
            return value
        for a, va in zip(ancestor[::-1], value_to_ancestor[::-1]):
            nu, nv = a[u], a[v]
            if nu == nv:
                continue
            value = monoid.op(value, va[u])
            value = monoid.op(value, va[v])
            u, v = nu, nv
        value = monoid.op(value, value_to_parent[u])
        value = monoid.op(value, value_to_parent[v])
        return value

    return get_value


def main() -> None:
    n = int(input())
    edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]
    q = int(input())
    res = []

    get = query_on_path_binary_lifting(
        Monoid(lambda x, y: x + y, lambda: 0),
        [(u, v, 1) for u, v in edges],
    )

    for _ in range(q):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        res.append(get(u, v) + 1)


    print(*res, sep='\n')

main()

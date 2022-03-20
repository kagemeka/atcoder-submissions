import typing
import sys

sys.setrecursionlimit(1 << 20)


def bfs_tree(
    graph: typing.List[typing.List[int]],
    root: int,
) -> typing.List[typing.Tuple[int, int]]:
    n = len(graph)
    tree_edges: typing.List[typing.Tuple[int, int]] = []

    added_to_que = [False] * n
    que = [root]
    added_to_que[root] = True
    for u in que:
        added_to_que[u] = True
        for v in graph[u]:
            if added_to_que[v]:
                continue
            tree_edges.append((u, v) if u < v else (v, u))
            que.append(v)
            added_to_que[v] = True
    return tree_edges


def main() -> None:
    n, m = map(int, input().split())
    uv = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

    g = [[] for _ in range(n)]
    for u, v in uv:
        g[u].append(v)
        g[v].append(u)

    s = list(map(int, input()))

    uv = bfs_tree(g, 0)

    g = [[] for _ in range(n)]
    for u, v in uv:
        g[u].append(v)
        g[v].append(u)

    # print(g)

    order = []
    # print(s)
    def dfs(u: int, parent: int) -> None:
        order.append(u)
        s[u] ^= 1
        for v in g[u]:
            if v == parent:
                continue
            dfs(v, u)
            order.append(u)
            s[u] ^= 1
            # print(s)
            if s[v] == 1:
                order.append(v)
                s[v] = 0
                order.append(u)
                s[u] ^= 1

    dfs(0, -1)
    if s[0] == 1:
        order.pop()
    order = [o + 1 for o in order]
    print(len(order))
    print(*order)

    # make bfs/dfs tree
    # before return check checked childs,
    # if odd/even is wrong, revisit them.
    # be careful root node


if __name__ == "__main__":
    main()

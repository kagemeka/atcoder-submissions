import typing


def _transpose_graph(
    graph: typing.List[typing.List[int]],
) -> typing.List[typing.List[int]]:
    n = len(graph)
    new_graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            new_graph[v].append(u)
    return new_graph


def kosaraju(graph: typing.List[typing.List[int]]) -> typing.List[int]:
    n = len(graph)
    visited = [False] * n
    que: typing.List[int] = []
    t_graph = _transpose_graph(graph)
    labels = [-1] * n
    label = 0

    def dfs(u: int) -> None:
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
        que.append(u)

    def rev_dfs(u: int, label: int):
        labels[u] = label
        for v in t_graph[u]:
            if labels[v] == -1:
                rev_dfs(v, label)

    for u in range(n):
        if not visited[u]:
            dfs(u)
    for u in que[::-1]:
        if labels[u] != -1:
            continue
        rev_dfs(u, label)
        label += 1
    return labels


# import functools
import sys

sys.setrecursionlimit(1 << 20)


def main() -> None:
    n, m = map(int, input().split())
    uv = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

    g = [[] for _ in range(n)]
    for u, v in uv:
        g[u].append(v)
        # g[v].append(u)
    labels = kosaraju(g)
    k = max(labels) + 1

    components = [[] for _ in range(k)]
    for i in range(n):
        components[labels[i]].append(i)

    to_cycle = [None] * n

    # @functools.lru_cache(maxsize=None)
    def dfs(u: int) -> bool:
        if to_cycle[u] is not None:
            return to_cycle[u]
        if len(components[labels[u]]) >= 2:
            to_cycle[u] = True
            return True
        # is_ok = False
        to_cycle[u] = False
        for v in g[u]:
            to_cycle[u] |= dfs(v)
            # is_ok |= dfs(v)
        return to_cycle[u]
        # return is_ok

    for i in range(n):
        to_cycle[i] = dfs(i)
    print(sum(to_cycle))


if __name__ == "__main__":
    main()

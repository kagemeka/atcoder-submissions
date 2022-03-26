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


def tarjan_lowlink(graph: typing.List[typing.List[int]]) -> typing.List[int]:
    n = len(graph)
    stack: typing.List[int] = []
    on_stack = [False] * n
    order = [-1] * n
    lowlink = [-1] * n
    ord = 0
    labels = [-1] * n
    label = 0

    def dfs(u: int) -> None:
        nonlocal ord, label
        order[u] = lowlink[u] = ord
        ord += 1
        stack.append(u)
        on_stack[u] = True
        for v in graph[u]:
            if order[v] == -1:
                dfs(v)
                lowlink[u] = min(lowlink[u], lowlink[v])
            elif on_stack[v] and order[v] < lowlink[u]:
                lowlink[u] = order[v]

        if lowlink[u] != order[u]:
            return
        while True:
            v = stack.pop()
            on_stack[v] = False
            labels[v] = label
            if v == u:
                break
        label += 1

    for i in range(n):
        if order[i] == -1:
            dfs(i)
    return labels


def path_based(graph: typing.List[typing.List[int]]) -> typing.List[int]:
    n = len(graph)
    order = [-1] * n
    labels = [-1] * n
    stack_0: typing.List[int] = []
    stack_1: typing.List[int] = []
    ord = 0
    label = 0

    def dfs(u: int) -> None:
        nonlocal ord, label
        order[u] = ord
        ord += 1
        stack_0.append(u)
        stack_1.append(u)
        for v in graph[u]:
            if order[v] == -1:
                dfs(v)
            elif labels[v] == -1:
                # v is start of a scc.
                while order[stack_0[-1]] > order[v]:
                    stack_0.pop()

        if stack_0[-1] != u:
            return
        while True:
            v = stack_1.pop()
            labels[v] = label
            # print(u, v)
            if v == u:
                break
        label += 1
        stack_0.pop()

    for i in range(n):
        if order[i] == -1:
            dfs(i)

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
    # labels = kosaraju(g)
    # labels = tarjan_lowlink(g)
    labels = path_based(g)
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

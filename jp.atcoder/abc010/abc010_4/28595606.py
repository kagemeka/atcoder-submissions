import typing


# O(EV^2)
def maxflow_dinic(
    capacity_graph: typing.List[typing.List[typing.Tuple[int, int]]],
    src: int,
    sink: int,
) -> int:
    n = len(capacity_graph)
    residual_flow = [[0] * n for _ in range(n)]
    for u in range(n):
        for v, capacity in capacity_graph[u]:
            residual_flow[u][v] += capacity

    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if residual_flow[u][v] > 0:
                graph[u].append(v)
    level = [-1] * n

    def update_level() -> None:
        nonlocal graph, level
        for i in range(n):
            level[i] = -1
        level[src] = 0
        que = [src]
        for u in que:
            for v in graph[u]:
                if level[v] != -1:
                    continue
                level[v] = level[u] + 1
                que.append(v)

    def flow_to_sink(u: int, flow_in: int) -> int:
        nonlocal residual_flow, graph, level
        if u == sink:
            return flow_in
        flow_out = 0
        edges = graph[u].copy()
        graph[u].clear()
        for v in edges:
            if level[v] == -1 or level[v] <= level[u]:
                graph[u].append(v)
                continue
            flow = flow_to_sink(v, min(flow_in, residual_flow[u][v]))
            residual_flow[u][v] -= flow
            if residual_flow[u][v] > 0:
                graph[u].append(v)
            if residual_flow[v][u] == 0 and flow > 0:
                graph[v].append(u)
            residual_flow[v][u] += flow
            flow_in -= flow
            flow_out += flow
        return flow_out

    inf = 1 << 63
    flow = 0
    while True:
        update_level()
        if level[sink] == -1:
            break
        flow += flow_to_sink(src, inf)
    return flow


# O(V^2 + Ef)
def maxflow_ford_fulkerson(
    capacity_graph: typing.List[typing.List[typing.Tuple[int, int]]],
    src: int,
    sink: int,
) -> int:
    n = len(capacity_graph)
    residual_flow = [[0] * n for _ in range(n)]
    for u in range(n):
        for v, capacity in capacity_graph[u]:
            residual_flow[u][v] += capacity

    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if residual_flow[u][v] > 0:
                graph[u].append(v)
    visited = [False] * n

    def augment_flow(u: int, flow_in: int) -> int:
        visited[u] = True
        if u == sink:
            return flow_in
        edges = graph[u].copy()
        graph[u].clear()
        flow = 0
        for v in edges:
            if visited[v] or flow > 0:
                graph[u].append(v)
                continue
            flow = augment_flow(v, min(flow_in, residual_flow[u][v]))
            residual_flow[u][v] -= flow
            if residual_flow[u][v] > 0:
                graph[u].append(v)
            if flow == 0:
                continue
            if residual_flow[v][u] == 0:
                graph[v].append(u)
            residual_flow[v][u] += flow
        return flow

    inf = 1 << 63
    flow = 0
    while True:
        for i in range(n):
            visited[i] = False
            f = augment_flow(src, inf)
            if f == 0:
                break
            flow += f
    return flow


# O(V^2 + VE^2)
def maxflow_edmonds_karp(
    capacity_graph: typing.List[typing.List[typing.Tuple[int, int]]],
    src: int,
    sink: int,
) -> int:
    n = len(capacity_graph)
    residual_flow = [[0] * n for _ in range(n)]
    for u in range(n):
        for v, capacity in capacity_graph[u]:
            residual_flow[u][v] += capacity

    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if residual_flow[u][v] > 0:
                graph[u].append(v)

    def find_path() -> typing.List[int]:
        parent = [-1] * n
        parent[src] = src
        que = [src]
        for u in que:
            graph[u] = [v for v in graph[u] if residual_flow[u][v] != 0]
            for v in graph[u]:
                if parent[v] != -1:
                    continue
                parent[v] = u
                que.append(v)
        v = sink
        path = [v]
        while parent[v] != -1 and v != src:
            v = parent[v]
            path.append(v)
        return path

    inf = 1 << 63

    def augment_flow(path: typing.List[int]) -> int:
        flow = inf
        for i in range(len(path) - 1):
            flow = min(flow, residual_flow[path[i + 1]][path[i]])
        assert flow != inf
        for i in range(len(path) - 1):
            u, v = path[i + 1], path[i]
            residual_flow[u][v] -= flow
            if residual_flow[v][u] == 0:
                graph[v].append(u)
            residual_flow[v][u] += flow
        return flow

    flow = 0
    while True:
        path = find_path()
        if len(path) == 1:
            break
        flow += augment_flow(path)
    return flow


def main() -> None:
    n, m, k = map(int, input().split())
    p = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]

    for x in p:
        graph[x].append((n, 1))

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    f = maxflow_dinic(graph, 0, n)
    print(f)

main()

import typing



def traveling_salesperson(
    graph: typing.List[typing.List[typing.Optional[int]]],
    src: int,
) -> typing.Optional[int]:
    # dist matrix
    n = len(graph)
    assert all(len(edges) == n for edges in graph)
    assert 0 <= src < n
    dist: typing.List[typing.List[typing.Optional[int]]] = [
        [None] * n for _ in range(1 << n)
    ]
    dist[1 << src][src] = 0
    for s in range(1 << n):
        for i in range(n):
            if ~s >> i & 1:
                continue
            t = s & ~(1 << i)
            for j in range(n):
                if ~t >> j & 1 or dist[t][j] is None or graph[j][i] is None:
                    continue
                d = dist[t][j] + graph[j][i]
                if dist[s][i] is None or d < dist[s][i]:
                    dist[s][i] = d

    mn: typing.Optional[int] = None
    for i in range(n):
        if i == src or dist[-1][i] is None or graph[i][src] is None:
            continue
        d = dist[-1][i] + graph[i][src]
        if mn is None or d < mn:
            mn = d
    return mn


def main() -> None:
    n = int(input())
    xyz = [tuple(map(int, input().split())) for _ in range(n)]

    graph: typing.List[typing.List[typing.Optional[int]]] = [
        [None] * n for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            xi, yi, zi = xyz[i]
            xj, yj, zj = xyz[j]
            graph[i][j] = abs(xj - xi) + abs(yj - yi) + max(0, zj - zi)

    res = traveling_salesperson(graph, 0)
    print(res)

main()

import typing
import math



def compute_dist(x0: int, y0: int, x1: int, y1: int) -> float:
    return math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)


Numeric = typing.Union[int, float]

# class Numeric(typing.Protocol):


def dijkstra_dense(
    g: typing.List[typing.List[Numeric]],
    src: int,
) -> typing.List[Numeric]:
    inf = 1 << 60
    n = len(g)
    assert 0 <= src < n
    for i in range(n):
        for j in range(n): assert g[i][j] >= 0
    dist = [inf] * n
    dist[src] = 0
    fixed = [False] * n
    # u = src
    for _ in range(n - 1):
        u, du = -1, inf
        for i in range(n):
            if fixed[i] or dist[i] >= du: continue
            u, du = i, dist[i]
        fixed[u] = True
        for v in range(n):
            dist[v] = min(dist[v], du + g[u][v])
    return dist




def main() -> typing.NoReturn:
    # calculate distances in all pairs with O(N^2).
    # O(N^2) dijkstra.
    sx, sy, gx, gy = map(int, input().split())
    n = int(input())
    xyr = [tuple(map(int, input().split())) for _ in range(n)]

    xyr.append((sx, sy, 0))
    xyr.append((gx, gy, 0))
    n += 2
    inf = 1 << 60
    dist = [[inf] * n for _ in range(n)]

    for i in range(n - 1):
        for j in range(i + 1, n):
            xi, yi, ri = xyr[i]
            xj, yj, rj = xyr[j]
            d = max(0, compute_dist(xi, yi, xj, yj) - ri - rj)
            dist[i][j] = dist[j][i] = d
    for i in range(n):
        dist[i][i] = 0

    dist = dijkstra_dense(dist, n - 2)
    print(dist[n - 1])


main()

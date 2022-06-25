# / mypy: ignore-errors
import typing


def main() -> None:
    n = int(input())

    a = [tuple(map(int, input().split())) for _ in range(n)]

    inf = 1 << 60
    g = [[inf] * n for _ in range(n)]

    for i in range(n):
        xi, yi, pi = a[i]
        for j in range(n):
            xj, yj, pj = a[j]
            d = abs(xi - xj) + abs(yi - yj)
            d = (d + pi - 1) // pi
            g[i][j] = d

    def calc_min(i: int) -> int:
        dist = [inf] * n
        dist[i] = 0
        is_fixed = [False] * n
        for _ in range(n - 1):
            u, du = None, inf
            for i in range(n):
                if is_fixed[i]:
                    continue
                if dist[i] < du:
                    u, du = i, dist[i]
            if u is None:
                break
            is_fixed[u] = True
            for v in range(n):
                if is_fixed[v]:
                    continue
                dv = g[u][v]
                if dv < dist[v]:
                    dist[v] = dv
        return max(dist)

    print(min(calc_min(i) for i in range(n)))


main()

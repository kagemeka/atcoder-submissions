# / mypy: ignore-errors
import typing


def debug(*objects: object, **kwargs: object) -> None:
    import os
    import pprint

    if os.environ.get("PYTHON_DEBUG") is None:
        return

    for obj in objects:
        pprint.pprint(obj)

    for key, obj in kwargs.items():
        print(f"{key}: ")
        pprint.pprint(obj)


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

    def possible(s: int) -> bool:
        dist = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dist[i][j] = g[i][j] if g[i][j] <= s else inf

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # print(dist)
        for i in range(n):
            row = dist[i]
            if all(d < inf for d in row):
                return True
        return False

    ng, ok = -1, inf
    while ok - ng > 1:
        s = (ok + ng) >> 1
        if possible(s):
            ok = s
        else:
            ng = s
    print(ok)


main()

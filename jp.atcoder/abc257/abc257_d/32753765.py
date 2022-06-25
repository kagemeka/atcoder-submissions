# / mypy: ignore-errors
import typing


T = typing.TypeVar("T")


G = typing.List[typing.List[T]]


def floyd_warshall(f: typing.Callable[[T, T, T], T], g: G) -> G:
    n = len(g)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = f(g[i][j], g[i][k], g[k][j])
    return g


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

    def f(x: int, y: int, z: int) -> int:
        return min(x, max(y, z))

    min_w = floyd_warshall(f, g)
    res = min(max(row) for row in min_w)
    print(res)


main()

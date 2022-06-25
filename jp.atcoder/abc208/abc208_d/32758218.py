# / mypy: ignore-errors
import typing


T = typing.TypeVar("T")
G = typing.List[typing.List[T]]
F = typing.Callable[[T, T, T], T]
Cb = typing.Callable[[int, G], None]


def floyd_warshall(f: F, g: G, cb: typing.Optional[Cb] = None) -> G:
    n = len(g)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = f(g[i][j], g[i][k], g[k][j])
        if cb:
            cb(k, g)
    return g


def main() -> None:
    n, m = map(int, input().split())
    inf = 1 << 60
    g = [[inf] * n for _ in range(n)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        g[a - 1][b - 1] = c
    for i in range(n):
        g[i][i] = 0

    s = 0

    def cb(_, g: G) -> None:
        nonlocal s
        for i in range(n):
            for j in range(n):
                if g[i][j] == inf:
                    continue
                s += g[i][j]

    def f(x: int, y: int, z: int) -> int:
        return min(x, y + z)

    floyd_warshall(f, g, cb)
    print(s)


main()

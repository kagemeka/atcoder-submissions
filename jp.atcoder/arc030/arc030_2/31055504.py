import typing
import sys

sys.setrecursionlimit(1 << 20)


def main() -> None:
    n, x = map(int, input().split())

    x -= 1
    h = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    def dfs(u: int, parent: int) -> typing.Tuple[int, int]:
        count = h[u]
        dist = 0
        for v in g[u]:
            if v == parent:
                continue
            c, d = dfs(v, u)
            if c == 0:
                continue
            count += c
            dist += d + 2
        return count, dist

    print(dfs(x, -1)[1])


if __name__ == "__main__":
    main()

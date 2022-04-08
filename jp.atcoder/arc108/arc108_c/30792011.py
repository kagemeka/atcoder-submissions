import sys

sys.setrecursionlimit(1 << 20)


def main() -> None:
    n, m = map(int, input().split())

    # make a rooted tree,

    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, c = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append((v, c))
        g[v].append((u, c))

    label = [-1] * n
    label[0] = 1

    def dfs(u: int, parent: int) -> None:
        for v, c in g[u]:
            if v == parent:
                continue
            if label[v] != -1:
                continue
            if label[u] == c:
                if c == 1:
                    label[v] = 2
                else:
                    label[v] = 1
            else:
                label[v] = c
            dfs(v, u)

    dfs(0, -1)
    print(*label, sep="\n")


if __name__ == "__main__":
    main()

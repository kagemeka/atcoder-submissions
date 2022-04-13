import sys

sys.setrecursionlimit(1 << 20)


def main() -> None:
    n, m = map(int, input().split())

    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, c = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append((v, c))
        g[v].append((u, c))

    labels = [-1] * n

    def labeling_childs(u: int) -> None:
        for v, c in g[u]:
            if labels[v] != -1:
                continue
            if c != labels[u]:
                labels[v] = c
            else:
                labels[v] = 1 if c != 1 else 2
            labeling_childs(v)

    labels[0] = 1
    labeling_childs(0)
    print(*labels, sep="\n")


if __name__ == "__main__":
    main()

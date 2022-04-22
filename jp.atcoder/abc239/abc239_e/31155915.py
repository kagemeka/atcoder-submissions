import sys

sys.setrecursionlimit(1 << 20)


def main() -> None:
    n, q = map(int, input().split())
    x = list(map(int, input().split()))

    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    value_lists = [[x[i]] for i in range(n)]
    K = 20

    def dfs(u: int, parent: int) -> None:
        for v in g[u]:
            if v == parent:
                continue
            dfs(v, u)
            value_lists[u] += value_lists[v]
        value_lists[u] = sorted(value_lists[u], reverse=True)[:K]

    dfs(0, -1)
    for _ in range(q):
        v, k = map(int, input().split())
        v -= 1
        print(value_lists[v][k - 1])


if __name__ == "__main__":
    main()

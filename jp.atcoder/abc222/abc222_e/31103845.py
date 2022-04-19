def main() -> None:
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(m):
        a[i] -= 1
    MOD = 998_244_353

    g = [[] for _ in range(n)]
    for edge_id in range(n - 1):

        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append((v, edge_id))
        g[v].append((u, edge_id))

    is_ancestor = [[False] * n for _ in range(n - 1)]

    edge_stack = []

    def check_ancestors(u: int, parent: int) -> None:
        for edge_id in edge_stack:
            is_ancestor[edge_id][u] = True
        for v, edge_id in g[u]:
            if v == parent:
                continue
            edge_stack.append(edge_id)
            check_ancestors(v, u)
            edge_stack.pop()

    check_ancestors(0, -1)

    passing_count = [0] * (n - 1)
    for i in range(m - 1):
        u, v = a[i], a[i + 1]
        for j in range(n - 1):
            passing_count[j] += is_ancestor[j][u] ^ is_ancestor[j][v]

    # r - b = k
    # r + b = sum(passing_count)

    s = sum(passing_count)

    if k + s < 0 or (k + s) & 1:
        print(0)
        return
    r = (k + s) >> 1
    if r - k < 0:
        print(0)
        return

    # r, b -> O(nm + k)
    # dp -> O((nm + k)n)
    dp = [0] * (r + 1)
    dp[0] = 1
    for c in passing_count:
        for i in range(r, c - 1, -1):
            dp[i] += dp[i - c]
            dp[i] %= MOD
    print(dp[-1])


if __name__ == "__main__":
    main()

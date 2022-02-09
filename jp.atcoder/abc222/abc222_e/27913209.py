import typing



def tree_bfs(
    g: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.Tuple[(typing.List[int], ) * 2]:
    n = len(g) + 1
    t = [[] for _ in range(n)]
    for u, v in g:
        t[u].append(v)
        t[v].append(u)
    depth = [0] * n
    parent = [-1] * n
    que = [root]
    for u in que:
        for v in t[u]:
            if v == parent[u]: continue
            parent[v] = u
            depth[v] = depth[u] + 1
            que.append(v)
    return parent, depth



def main() -> typing.NoReturn:
    n, m, k = map(int, input().split())
    a = list(map(lambda x: int(x) - 1, input().split()))
    uv = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]

    MOD = 998_244_353

    idx = {}
    for i, (u, v) in enumerate(uv):
        if u > v: u, v = v, u
        idx[(u, v)] = i

    cnt = [0] * (n - 1)
    for i in range(m - 1):
        root, u = a[i], a[i + 1]

        parent, _ = tree_bfs(uv, root)
        while u != root:
            p = parent[u]
            v = p
            if u > v:
                u, v = v, u
            cnt[idx[(u, v)]] += 1
            u = p
    sc = sum(cnt)
    cand = [c for c in cnt if c > 0]
    if (k + sc) % 2 == 1:
        print(0)
        return
    r = (k + sc) // 2
    if r < k or r < 0:
        print(0)
        return
    dp = [0] * (r + 1)
    dp[0] = 1
    for x in cand:
        for i in range(r, x - 1, -1):
            dp[i] += dp[i - x]
            dp[i] %= MOD

    ans = dp[r] * pow(2, n - 1 - len(cand)) % MOD
    print(ans)

main()

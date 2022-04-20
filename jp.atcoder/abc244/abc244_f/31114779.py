def main() -> None:
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    INF = 1 << 60
    min_length = [INF] * (1 << n)
    remain = 1 << n
    min_length[0] = 0
    remain -= 1
    # bfs
    dp = [[INF] * n for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i][i] = 1

    current_length = 1
    que = [(1 << i, i) for i in range(n)]
    while remain:
        new_que = []
        for s, i in que:
            if min_length[s] == INF:
                min_length[s] = current_length
                remain -= 1
            for j in g[i]:
                t = s ^ (1 << j)
                if dp[t][j] != INF:
                    continue
                dp[t][j] = current_length
                new_que.append((t, j))
        current_length += 1
        que = new_que
    print(sum(min_length))


if __name__ == "__main__":
    main()

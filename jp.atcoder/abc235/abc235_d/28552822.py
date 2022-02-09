import typing


def main() -> None:
    a, n = map(int, input().split())

    k = 1 << 20
    g = [[] for _ in range(k)]
    for i in range(1, k):
        if a * i < k:
            g[i].append(a * i)
        if i < 10 or i % 10 == 0: continue
        j = str(i)
        j = int(j[-1] + j[:-1])
        if j < k:
            g[i].append(j)

    que = [1]
    inf = 1 << 20
    dist = [inf] * k
    dist[1] = 0
    for u in que:
        for v in g[u]:
            dv = dist[u] + 1
            if dv >= dist[v]: continue
            dist[v] = dv
            que.append(v)

    d = dist[n]
    print(-1 if d == inf else d)

main()

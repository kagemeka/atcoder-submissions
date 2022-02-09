import typing


def main() -> typing.NoReturn:
    n = int(input())
    # DAG
    # longest path
    # if a cycle found, impossible.
    k = 1 << 20
    g = [[] for _ in range(k)]
    in_deg = [0] * k
    for i in range(n):
        a = list(map(int, input().split()))
        for j in range(n - 2):
            x, y = a[j], a[j + 1]
            x -= 1
            y -= 1
            x = i * n + x if i < x else x * n + i
            y = i * n + y if i < y else y * n + i
            g[x].append(y)
            in_deg[y] += 1

    que = [i for i in range(k) if in_deg[i] == 0]
    dist = [0] * k
    for u in que:
        for v in g[u]:
            dist[v] = max(dist[v], dist[u] + 1)
            in_deg[v] -= 1
            if in_deg[v] == 0:
                que.append(v)
    if any(d > 0 for d in in_deg):
        print(-1)
        return
    print(max(dist) + 1)


main()

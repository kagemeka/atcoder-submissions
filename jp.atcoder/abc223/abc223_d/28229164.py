import typing
import heapq

def main() -> typing.NoReturn:
    n, m = map(int, input().split())

    # DAG
    # if not DAG, there is no permutation satisfying the given constraints.


    g = [[] for _ in range(n)]
    in_deg = [0] * n
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        in_deg[b] += 1


    hq = []
    for i in range(n):
        if in_deg[i] == 0:
            heapq.heappush(hq, i)


    res = []
    while hq:
        u = heapq.heappop(hq)
        res.append(u)
        for v in g[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                heapq.heappush(hq, v)
    assert len(res) <= n
    if len(res) < n:
        print(-1)
    else:
        print(*[x + 1 for x in res])

main()

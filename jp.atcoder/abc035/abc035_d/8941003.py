import sys
from heapq import heappush, heappop

n, m, T = map(int, sys.stdin.readline().split())
*point, = map(int, sys.stdin.readline().split())
abc = map(int, sys.stdin.read().split())
abc = list(zip(abc, abc, abc))

g_a2x = [[] for _ in range(n)]
g_x2a = [[] for _ in range(n)]
for a, b, c in abc:
    g_a2x[a-1].append((b-1, c))
    g_x2a[b-1].append((a-1, c))

INF = 10 ** 18
def dijkstra(g):
    visited = set()
    hq = []
    heappush(hq, (0, 0))
    time = [INF] * n
    while hq:
        shortest, i = heappop(hq)
        if i in visited:
            continue
        visited.add(i)
        time[i] = shortest
        for j, t in g[i]:
            if j in visited:
                continue
            heappush(hq, (shortest + t, j))
    return time

def main():
    t_a2x = dijkstra(g_a2x)
    t_x2a = dijkstra(g_x2a)
    time = [None] * n
    for i in range(n):
        time[i] = t_a2x[i] + t_x2a[i]

    money = [None] * n
    for i in range(n):
        money[i] = point[i] * max(T - time[i], 0)

    ans = max(money)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

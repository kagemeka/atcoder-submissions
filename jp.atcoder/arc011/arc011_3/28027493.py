import typing
import sys
import collections


def main() -> typing.NoReturn:
    s, t = input().split()
    n = int(input())
    a = sys.stdin.read().split()
    m = len(s)
    a = [s] + a + [t]
    n += 2

    g = [[] for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            s, t = a[i], a[j]
            diff = sum(s[k] != t[k] for k in range(m))
            if diff >= 2: continue
            g[i].append((j, diff))
            g[j].append((i, diff))

    que = collections.deque()
    que.append(0)
    inf = 1 << 60
    dist = [inf] * n
    dist[0] = 0
    prev = [-1] * n
    while que:
        u = que.popleft()
        for v, w in g[u]:
            d = dist[u] + w
            if d >= dist[v]: continue
            dist[v] = d
            prev[v] = u
            if w:
                que.append(v)
            else:
                que.appendleft(v)

    if prev[n - 1] == -1:
        print(-1)
        return
    res = []
    u = n - 1
    while u != -1:
        res.append(u)
        u = prev[u]

    print(len(res) - 2)
    for i in res[::-1]:
        print(a[i])


main()

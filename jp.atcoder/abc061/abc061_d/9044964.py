import sys

inf = float('inf')

n, m = map(int, sys.stdin.readline().split())
a = []
b = []
c = []
for _ in range(m):
    ai, bi, ci = map(int, sys.stdin.readline().split())
    a.append(ai - 1)
    b.append(bi - 1)
    c.append(-ci)
abc = list(zip(a, b, c))

def main():
    dist = [inf] * n
    dist[0] = 0
    for _ in range(n-1):
        for a, b, c in abc:
            dist[b] = min(dist[b], dist[a] + c)

    res = dist[n-1]

    for _ in range(n):
        for a, b, c in abc:
            dist[b] = min(dist[b], dist[a] + c)

    if dist[n-1] == res:
        return -res
    else:
        return 'inf'

if __name__ == '__main__':
    ans = main()
    print(ans)

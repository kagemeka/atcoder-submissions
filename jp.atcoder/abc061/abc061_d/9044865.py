import sys

INF = 10 ** 15

n, m = map(int, sys.stdin.readline().split())
abc = map(int, sys.stdin.read().split())
abc = list(zip(*[abc] * 3))

def main():
    dist = [INF] * n
    dist[0] = 0
    for _ in range(n - 1):
        for a, b, c in abc:
            a -= 1; b -= 1; c = -c
            if dist[a] == INF:
                continue
            dist[b] = min(dist[b], dist[a] + c)

    res = dist[n-1]

    for _ in range(n - 1):
        for a, b, c in abc:
            a -= 1; b -= 1; c = -c
            if dist[a] == INF:
                continue
            dist[b] = min(dist[b], dist[a] + c)

    if dist[n-1] == res:
        return -res
    else:
        return 'inf'

if __name__ == '__main__':
    ans = main()
    print(ans)

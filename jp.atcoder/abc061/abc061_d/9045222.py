import sys

inf = float('inf')

n, m = map(int, sys.stdin.readline().split())
abc = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    abc.append((a-1, b-1, -c))

def main():
    dist = [inf] * n
    dist[0] = 0
    for _ in range(n-1):
        for a, b, c in abc:
            dist[b] = min(dist[b], dist[a] + c)

    for _ in range(n):
        for a, b, c in abc:
            if dist[a] + c < dist[b]:
                dist[b] = -inf

    return -dist[n-1]

if __name__ == '__main__':
    ans = main()
    print(ans)

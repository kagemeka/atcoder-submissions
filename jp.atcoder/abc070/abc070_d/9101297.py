import sys

n = int(sys.stdin.readline().rstrip())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a].append((b, c))
    g[b].append((a, c))

q, k = map(int, sys.stdin.readline().split())
xy = zip(*[map(int, sys.stdin.read().split())] * 2)

def dfs(v):
    dist = [None] * (n + 1)
    stack = [(v, 0)]
    while stack:
        x, d = stack.pop()
        dist[x] = d
        for y, dd in g[x]:
            if dist[y] is None:
                stack.append((y, d + dd))
    return dist

def main():
    dist_k = dfs(k)

    for x, y in xy:
        yield dist_k[x] + dist_k[y]

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')

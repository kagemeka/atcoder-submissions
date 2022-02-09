import sys

n, u, v, *ab = map(int, sys.stdin.read().split())
graph = [[] for _ in range(n+1)]
for a, b in zip(*[iter(ab)] * 2):
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    dist = [None] * (n + 1)
    dist[v] = 0
    stack = [v]
    while stack:
        x = stack.pop()
        for y in graph[x]:
            if dist[y] is None:
                dist[y] = dist[x] + 1
                stack.append(y)
    return dist

def main():
    dist_u = dfs(u)
    dist_v = dfs(v)

    d = 1
    for i in range(1, n+1):
        if dist_v[i] >= dist_u[i]:
            d = max(d, dist_v[i])
    ans = d - 1
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

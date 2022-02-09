import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for l, r, d in zip(*[map(int, sys.stdin.read().split())] * 3):
    graph[l].append((r, d))
    graph[r].append((l, -d))

root = list(range(n+1))
height = [0] * (n + 1)

def find_root(v):
    u = root[v]
    if u == v:
        return u
    w = find_root(u)
    root[v] = w
    return w

def merge(v, u):
    rv = find_root(v)
    ru = find_root(u)
    if rv != ru:
        if height[v] >= height[u]:
            root[ru] = rv
            height[v] = max(height[v], height[v] + 1)
        else:
            root[rv] = ru

def main():
    for v in range(1, n+1):
        for u, d in graph[v]:
            merge(v, u)

    dist = [None] * (n + 1)
    for v in set(root[1:]):
        dist[v] = 0
        stack = [v]
        while stack:
            x = stack.pop()
            for y, d in graph[x]:
                if dist[y] is None:
                    dist[y] = dist[x] + d
                    stack.append(y)
                elif dist[y] != dist[x] + d:
                    return 'No'
    return 'Yes'

if __name__ == '__main__':
    ans = main()
    print(ans)

import sys

n, m, k = map(int, sys.stdin.readline().split())
ab = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
cd = [tuple(map(int, sys.stdin.readline().split())) for _ in range(k)]
friend = [set() for _ in range(n+1)]
for a, b in ab:
    friend[a].add(b)
    friend[b].add(a)
block = [set() for _ in range(n+1)]
for c, d in cd:
    block[c].add(d)
    block[d].add(c)

root = list(range(n+1))
size = [1] * (n + 1)
height = [1] * (n + 1)

def find_root(u):
    v = root[u]
    if v == u:
        return u
    w = find_root(v)
    root[u] = w
    return w

def unite(u, v):
    ru = find_root(u)
    rv = find_root(v)
    if ru != rv:
        if height[ru] >= height[rv]:
            root[rv] = ru
            height[ru] = max(height[ru], height[rv] + 1)
            size[ru] += size[rv]
        else:
            root[ru] = rv
            size[rv] += size[ru]

def main():
    for u in range(1, n+1):
        for v in friend[u]:
            unite(u, v)

    g = [set() for _ in range(n+1)]
    for i in range(1, n+1):
        find_root(i)
        g[root[i]].add(i)

    for i in range(1, n+1):
        yield len(g[root[i]] - friend[i] - block[i]) - 1

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')

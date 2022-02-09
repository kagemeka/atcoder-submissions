import sys

n, m, k = map(int, sys.stdin.readline().split())
ab = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
cd = [tuple(map(int, sys.stdin.readline().split())) for _ in range(k)]
friend = [[] for _ in range(n+1)]
for a, b in ab:
    friend[a].append(b)
    friend[b].append(a)
block = [[] for _ in range(n+1)]
for c, d in cd:
    block[c].append(d)
    block[d].append(c)

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

    for u in range(1, n+1):
        find_root(u)

    for u in range(1, n+1):
        ru = root[u]
        cnt = size[ru] - 1  - len(friend[u])
        for v in block[u]:
            if root[v] == ru:
                cnt -= 1
        yield cnt

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')

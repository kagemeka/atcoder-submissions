import sys

n, m = map(int, sys.stdin.readline().split())
*p, = map(int, sys.stdin.readline().split())
xy = list(zip(*[map(int, sys.stdin.read().split())] * 2))

g = [[] for _ in range(n+1)]
for x, y in xy:
    g[x-1].append(y-1)
    g[y-1].append(x-1)

root = list(range(n))
height = [0] * n

def find_root(v):
    u = root[v]
    if u == v:
        return u
    w = find_root(u)
    root[v] = w
    return w

def unite(v, u):
    rv = find_root(v)
    ru = find_root(u)
    if root[rv] == root[ru]:
        return
    if height[rv] >= height[ru]:
        root[ru] = rv
        height[rv] = max(height[rv], ru+1)
    else:
        root[rv] = ru

def main():
    for x, y in xy:
        unite(x-1, y-1)

    for i in range(n):
        find_root(i)

    cnt = 0
    for i in range(n):
        cnt += (root[i] == root[p[i]-1]) & 1

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)

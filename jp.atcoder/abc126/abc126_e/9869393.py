import sys

n, m, *xyz = map(int, sys.stdin.read().split())
xyz = zip(*[iter(xyz)] * 3)

root = list(range(n+1))
height = [0] * (n + 1)

sys.setrecursionlimit(10**7)
def find_root(v):
    u = root[v]
    if u == v:
        return u
    w = find_root(u)
    root[v] = w
    return w

def unite(u, v):
    ru = find_root(u)
    rv = find_root(v)
    if ru == rv:
        return
    if height[u] >= height[v]:
        root[rv] = ru
        height[ru] = max(height[ru], height[rv] + 1)
    else:
        root[ru] = rv

def main():
    for x, y, z in xyz:
        unite(x, y)

    for i in range(1, n+1):
        find_root(i)

    return len(set(root[1:]))

if __name__ == '__main__':
    ans = main()
    print(ans)

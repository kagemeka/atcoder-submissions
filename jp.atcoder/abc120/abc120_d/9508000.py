import sys

n, m, *ab = map(int, sys.stdin.read().split())
ab = list(zip(*[iter(ab)] * 2))

root = list(range(n+1)); root[0] = None
height = [0] * (n + 1); height[0] = None
size = [1] * (n + 1); size[0] = None

sys.setrecursionlimit(10 ** 9)
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
    if rv == ru:
        return 0
    sv = size[rv]
    su = size[ru]
    if height[v] >= height[u]:
        root[ru] = rv
        height[rv] = max(height[rv], height[ru] + 1)
        size[rv] += size[ru]
    else:
        root[rv] = ru
        size[ru] += size[rv]
    return sv * su

def main():
    res = [0] * m
    for i in range(1, m):
        res[i] = res[i-1] + unite(*ab[m-i])

    all_pairs = n * (n - 1) // 2
    for i in res[::-1]:
        yield all_pairs - i

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')

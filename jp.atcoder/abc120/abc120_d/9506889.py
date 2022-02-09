import sys

n, m, *ab = map(int, sys.stdin.read().split())
ab = list(zip(*[iter(ab)] * 2))

root = list(range(n+1)); root[0] = None
height = [0] * (n + 1); height[0] = None
size = [1] * (n + 1); size[0] = None

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
        return
    if height[v] >= height[u]:
        root[ru] = rv
        height[rv] = max(height[rv], height[ru] + 1)
        size[rv] += size[ru]
    else:
        root[rv] = ru
        size[ru] += size[rv]

def is_alone(v, rv, sv):
    return v == rv and sv == 1

def main():
    res = [0] * (m + 1)
    for i in range(1, m):
        a, b = ab[m-i]
        ra = find_root(a)
        rb = find_root(b)
        sa = size[ra]
        sb = size[rb]

        bl_a = is_alone(a, ra, sa)
        bl_b = is_alone(b, rb, sb)

        if bl_a & bl_b:
            res[i+1] = res[i] + 1
        elif bl_a ^ bl_b:
            res[i+1] = res[i] + sa * sb
        else:
            if ra == rb:
                res[i+1] = res[i]
            else:
                res[i+1] = res[i] + sa * sb

        unite(a, b)

    res = res[::-1]
    all_pairs = n * (n - 1) // 2
    for i in range(m):
        yield all_pairs - res[i]

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')

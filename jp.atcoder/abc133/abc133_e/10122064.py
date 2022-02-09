import sys

MOD = 10**9 + 7

n, k, *ab = map(int, sys.stdin.read().split())
ab = zip(*[iter(ab)] * 2)
g = [[] for _ in range(n+1)]
for a, b in ab:
    g[a].append(b)
    g[b].append(a)

def main():
    stack = [1]
    coloring = [None] * (n + 1); coloring[1] = k
    par = [None] * (n + 1)
    while stack:
        u = stack.pop()
        r = k - 1
        if par[u]:
            r -= 1
        for v in g[u]:
            if v != par[u]:
                par[v] = u
                if r < 0:
                    return 0
                coloring[v] = r
                r -= 1
                stack.append(v)

    res = 1
    for i in range(1, n+1):
        res *= coloring[i]
        res %= MOD

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)

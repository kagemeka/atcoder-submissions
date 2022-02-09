import sys

n, q = map(int, sys.stdin.readline().split())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)

px = zip(*[map(int, sys.stdin.read().split())] * 2)

def main():
    value = [0] * (n + 1)
    for p, x in px:
        value[p] += x

    stack = [1]
    par = [None] * (n + 1)
    while stack:
        u = stack.pop()
        for v in g[u]:
            if v != par[u]:
                par[v] = u
                value[v] += value[u]
                stack.append(v)

    return value[1:]

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')

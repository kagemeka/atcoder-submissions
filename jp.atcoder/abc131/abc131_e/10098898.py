import sys

n, k = map(int, sys.stdin.readline().split())

def main():
    r = (n - 1) * (n - 2) // 2 - k
    if r < 0:
        return [[-1]]

    edges = [(1, v) for v in range(2, n+1)]
    m = n - 1 + r

    u = 2; v = 3
    for _ in range(r):
        edges.append((u, v))
        v += 1
        if v == n + 1:
            u += 1
            v = u + 1

    res = [[m]] + edges
    return res

if __name__ == '__main__':
    ans = main()
    for a in ans:
        print(*a, sep=' ')

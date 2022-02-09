import sys

n, k, l = map(int, sys.stdin.readline().split())
roads = [tuple(map(lambda x: int(x) - 1, sys.stdin.readline().split())) for _ in range(k)]
railways = [tuple(map(lambda x: int(x) - 1, sys.stdin.readline().split())) for _ in range(l)]

reach_road = [set([i]) for i in range(n)]
reach_rail = [set([i]) for i in range(n)]

def union(v, u, kind):
    if kind == 'ro':
        reach_road[v] |= reach_road[u]
        reach_road[u] = reach_road[v]
    elif kind == 'ra':
        reach_rail[v] |= reach_rail[u]
        reach_rail[u] = reach_rail[v]

def main():
    for v, u in roads:
        union(v, u, 'ro')

    for v, u in railways:
        union(v, u, 'ra')

    res = [None] * n
    for i in range(n):
        res[i] = len(reach_road[i] & reach_rail[i])
    return res

if __name__ == '__main__':
    ans = main()
    print(*ans)

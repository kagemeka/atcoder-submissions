import sys
from itertools import combinations

n, m, *xy = map(int, sys.stdin.read().split())
xy = zip(*[iter(xy)] * 2)
g = [set() for _ in range(n+1)]
for x, y in xy:
    g[x-1].add(y-1)

def main():
    res = 1
    for i in range(2**n):
        group = [j for j in range(n) if i >> j & 1]
        for x, y in combinations(group, 2):
            if not y in g[x]:
                break
        else:
            res = max(res, len(group))
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)

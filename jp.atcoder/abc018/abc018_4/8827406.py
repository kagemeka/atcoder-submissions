import sys
from itertools import combinations

n, m, p, q, r = map(int, sys.stdin.readline().split())
xyz = map(int, sys.stdin.read().split())
xyz = list(zip(xyz, xyz, xyz))
graph = [[0] * (m + 1) for _ in range(n + 1)]
for x, y, z in xyz:
    graph[x][y] = z

def main():
    ans = 0
    for comb in combinations(range(1, n + 1), p):
        res = [0] * (m + 1)
        for x in comb:
            for y in range(1, m + 1):
                res[y] += graph[x][y]

        ans = max(ans, sum(sorted(res)[-q:]))

    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

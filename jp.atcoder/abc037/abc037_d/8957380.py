import sys
from collections import defaultdict

MOD = 10 ** 9 + 7

h, w = map(int, sys.stdin.readline().split())
grid = [[0] * (w + 2)] + [[0] + [int(x) for x in sys.stdin.readline().split()] + [0] for _ in range(h)] + [[0] * (w + 2)]

def main():
    for i in range(h + 2):
        print(grid[i])
    places = defaultdict(list)
    for i in range(1, h+1):
        for j in range(1, w+1):
            places[grid[i, j]].append((i, j))

    return 'TLE?'


    # res = np.zeros((h+2, w+2), dtype=np.int64)
    # res[1:h+1, 1:w+1] = 1
    # ans = 0
    # for indices in places.values():
    #     for i, j in indices:
    #         for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    #             y = i + dy
    #             x = j + dx
    #             if grid[y, x] < grid[i, j]:
    #                 res[i, j] += res[y, x]
    #         res[i, j] %= MOD
    #         ans += res[i, j]
    #         ans %= MOD

    # return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

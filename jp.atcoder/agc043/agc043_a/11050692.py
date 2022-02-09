import sys

h, w = map(int, sys.stdin.readline().split())
grid = [sys.stdin.readline().rstrip() for _ in range(h)]

def main():
    cost = [[0] * w for _ in range(h)]
    cost[0][0] = 1 if grid[0][0] == '#' else 0
    for j in range(1, w):
        cost[0][j] = cost[0][j-1]
        if grid[0][j] == '#':
            if grid[0][j-1] == '.':
                cost[0][j] += 1

    for i in range(1, h):
        cost[i][0] = cost[i-1][0]
        if grid[i][0] == '#':
            if grid[i-1][0] == '.':
                cost[i][0] += 1

    for i in range(1, h):
        for j in range(1, w):
            c1 = cost[i][j-1]
            if grid[i][j] == '#':
                if grid[i][j-1] == '.':
                    c1 += 1
            c2 = cost[i-1][j]
            if grid[i][j] == '#':
                if grid[i-1][j] == '.':
                    c2 += 1

            cost[i][j] = min(c1, c2)
    return cost[h-1][w-1]

if __name__ == "__main__":
    ans = main()
    print(ans)

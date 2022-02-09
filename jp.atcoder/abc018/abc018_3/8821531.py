import sys

R, C, K = map(int, sys.stdin.readline().split())
grid = sys.stdin.read().split()

def main():
    if R + 1 < 2 * K or C + 1 < 2 * K:
        return 0

    l = [[0] * C for _ in range(R)]
    r = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(1, C):
            if grid[x][y-1] == 'o':
                l[x][y] = l[x][y-1] + 1

    for x in range(R):
        for y in range(C-2, -1, -1):
            if grid[x][y+1] == 'o':
                r[x][y] = r[x][y+1] + 1


    cnt = 0
    for x in range(K-1, R - K + 1):
        for y in range(K-1, C - K + 1):
            for dx in range(-K+1, K):
                i = x + dx
                if grid[i][y] == 'x':
                    break
                if l[i][y] < K - 1 - abs(dx) or r[i][y] < K - 1 - abs(dx):
                    break
            else:
                print(x, y)
                cnt += 1
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)

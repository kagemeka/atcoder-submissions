import sys

R, C, K = map(int, sys.stdin.readline().split())
grid = sys.stdin.read().split()

def main():
    if R + 1 < 2 * K or C + 1 < 2 * K:
        return 0

    cnt = 0
    for x in range(K-1, R - K + 1):
        for y in range(K-1, C - K + 1):
            flag = False
            for dx in range(-K+1, K):
                for dy in range(-(K-1-abs(dx)), K - abs(dx)):
                    i = x + dx
                    j = y + dy
                    if grid[i][j] == 'x':
                        flag = True
                        break
                if flag:
                    break
            else:
                cnt += 1
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)

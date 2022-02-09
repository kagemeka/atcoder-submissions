import sys
import numpy as np

I = np.array(sys.stdin.read().split())
R, C, K = I[:3].astype(np.int64)
grid = np.array([list(w) for w in I[3:]])
grid = np.pad(grid, 1, mode='constant')

def main():
    if R + 1 < 2 * K or C + 1 < 2 * K:
        return 0

    res = np.zeros((R + 2, C + 2))
    res -= 1
    res[grid == 'o'] = np.inf

    for y in range(1, C + 1):
        np.minimum(res[:, y - 1] + 1, res[:, y], out=res[:, y])
    for y in range(C, 0, -1):
        np.minimum(res[:, y + 1] + 1, res[:, y], out=res[:, y])

    cnt = 0
    for x in range(K, R - K + 2):
        for y in range(K, C - K + 2):
            for dx in range(-K+1, K):
                i = x + dx
                if res[i][y] < K - 1 - abs(dx):
                    break
            else:
                cnt += 1
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)

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

    for x in range(1, R + 1):
        np.minimum(res[x - 1] + 1, res[x], out=res[x])
    for x in range(R, 0, -1):
        np.minimum(res[x + 1] + 1, res[x], out=res[x])
    for y in range(1, C + 1):
        np.minimum(res[:, y - 1] + 1, res[:, y], out=res[:, y])
    for y in range(C, 0, -1):
        np.minimum(res[:, y + 1] + 1, res[:, y], out=res[:, y])

    return np.count_nonzero(res >= K - 1)

if __name__ == '__main__':
    ans = main()
    print(ans)

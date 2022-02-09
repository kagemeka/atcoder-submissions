# 2019-11-25 16:19:29(JST)
import sys
import numpy as np

def main():
    H, W, K = map(int, sys.stdin.readline().split())
    N = int(sys.stdin.readline().rstrip())
    hw = map(int, sys.stdin.read().split())
    hw = list(zip(hw, hw))

    vert, hori = [0] * (H + 1), [0] * (W + 1)
    candy = [[0] * (W + 1) for _ in range(H + 1)]
    for h, w in hw:
        candy[h][w] = 1
        vert[h] += 1
        hori[w] += 1


    a = np.array([1, 3, 4, 5, 6])
    b = np.array([1, 3, 4, 5, 7])

    res = np.array([vert[i] + hori[j] - candy[i][j] for i in range(1, H+1) for j in range(1, W + 1)])
    res.sort()

    ans = np.searchsorted(res, K, side='right') - np.searchsorted(res, K, side='left')
    print(ans)

if __name__ == '__main__':
    main()

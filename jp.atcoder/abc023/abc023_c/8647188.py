# 2019-11-25 16:19:29(JST)
import sys
import numpy as np

def main():
    H, W, K = map(int, sys.stdin.readline().split())
    N = int(sys.stdin.readline().rstrip())
    hw = map(int, sys.stdin.read().split())
    hw = list(zip(hw, hw))

    candy = np.array([np.zeros(W+1, dtype=np.int64) for _ in range(H+1)])

    for h, w in hw:
        candy[h] += 1
        candy = candy.T
        candy[w] += 1
        candy = candy.T
        candy[h][w] -= 1

    res = np.sort(candy.ravel())

    ans = np.searchsorted(res, K, side='right') - np.searchsorted(res, K, side='left')
    print(ans)

if __name__ == '__main__':
    main()

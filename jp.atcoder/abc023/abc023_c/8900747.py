import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
R, C, K, n = I[:4]
r, c = I[4:].reshape(-1, 2).T - 1

def main():
    y_cnt = np.bincount(r, minlength=R)
    x_cnt = np.bincount(c, minlength=C)
    cnt_y_cnt = np.bincount(y_cnt, minlength=K+1)
    cnt_x_cnt = np.bincount(x_cnt, minlength=K+1)

    res = np.sum(cnt_y_cnt[:K+1] * cnt_x_cnt[K::-1])
    real_cnt =  y_cnt[r] + x_cnt[c] - 1 # (grid[r][c]からみた本当の飴の数)
    cnt_real_cnt = np.bincount(real_cnt, minlength=K+1)
    ans = res + cnt_real_cnt[K] - cnt_real_cnt[K-1]
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

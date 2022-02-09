import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, m = I[:2]
a = I[2:]
a.sort()
ma = a[-1]
cnt = np.bincount(a, minlength=ma+2)
cnt_not_less_than = np.cumsum(cnt[::-1])[::-1]

right = a[:, None]
def possible(border):
    left = border - right
    left = np.maximum(left, 0)
    left = np.minimum(left, ma+1)
    pair_cnt = np.sum(cnt_not_less_than[left])
    return pair_cnt >= m

def main():
    lo = 1; hi = ma * 2 + 1
    while lo + 1 < hi:
        border = (lo + hi) // 2
        if possible(border):
            lo = border
        else:
            hi = border

    res = lo
    left = res - right
    left = np.maximum(left, 0)
    left = np.minimum(left, ma+1)
    c = cnt_not_less_than[left[left != ma+1]]
    pair_cnt = np.sum(c)
    minimum = np.amin(right[left != ma + 1] + a[-c])

    s = np.cumsum(a[::-1])
    ans = np.sum(s[c-1] + right[left != ma+1] * c) - minimum * (pair_cnt - m)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

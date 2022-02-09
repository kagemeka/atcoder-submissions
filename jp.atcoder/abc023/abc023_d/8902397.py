import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n = I[0]
h, s = I[1:].reshape(-1, 2).T

b = np.arange(n)
def is_ok(x):
    t_limit = (x - h) // s
    t_limit = np.sort(t_limit)
    # bincount + cumsumでO(n)だが、
    # bincountがmaxlengthを指定できずMLEになるので止むを得ずsort。
    return np.all(t_limit >= b)

INF = 10 ** 15

def main():
    lo = np.amin(h)
    hi = INF
    while lo + 1 < hi:
        x = (lo + hi) // 2
        if is_ok(x):
            hi = x
        else:
            lo = x
    return hi

if __name__ == '__main__':
    ans = main()
    print(ans)

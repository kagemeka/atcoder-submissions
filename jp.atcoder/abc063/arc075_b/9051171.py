import sys
import numpy as np

n, a, b = map(int, sys.stdin.readline().split())
h = np.array(sys.stdin.read().split(), dtype=np.int64)
r = a - b

def can_vanish_all(c):
    res = np.copy(h)
    res = np.maximum(res - b * c, 0)
    res = (res + r - 1) // r
    return np.sum(res) <= c

def main():
    lo = 0 # 不可能最大
    hi = 10**9+1 # 可能最小
    while lo + 1 < hi:
        cnt = (lo + hi) // 2
        if can_vanish_all(cnt):
            hi = cnt
        else:
            lo = cnt

    return hi

if __name__ == '__main__':
    ans = main()
    print(ans)

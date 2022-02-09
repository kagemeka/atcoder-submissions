# 2019-11-28 00:36:19(JST)
import sys
import numpy as np
def main():
    n = int(sys.stdin.readline().rstrip())
    ab = np.array(sys.stdin.read().split(), dtype=np.int64)
    a = ab[::2]
    b = ab[1::2]

    cnt = 0
    for i in range(n-1, -1, -1):
        x = a[i] + cnt
        y = b[i]
        if x % y != 0:
            cnt += y - x % y

    print(cnt)

if __name__ == '__main__':
    main()

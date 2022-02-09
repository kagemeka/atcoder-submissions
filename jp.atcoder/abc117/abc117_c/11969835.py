import sys
import numpy as np

n, m = map(int, sys.stdin.readline().split())
x = np.array(sys.stdin.readline().split(), dtype=np.int64)
x.sort()

def main():
    if n >= m:
        print(0)
        return
    d = x[1:] - x[:-1]
    d = np.sort(d)[::-1]
    np.cumsum(d, out=d)
    res = d[-1]
    res -= 0 if n == 1 else d[n-2]
    print(res)

if __name__ ==  '__main__':
    main()

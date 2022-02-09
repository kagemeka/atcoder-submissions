import sys
import numpy as np

n, *c = map(int, sys.stdin.read().split())

def main():
    lis = np.full(n, np.inf)

    res = n - 1
    for i in range(n):
        res = np.searchsorted(lis, c[i], side='left')
        lis[res] = c[i]

    ans = n - res - 1
    print(ans)

if __name__ == '__main__':
    main()

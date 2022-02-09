import sys
import numpy as np

n, *c = map(int, sys.stdin.read().split())

def main():
    lis = np.full(n, np.inf)

    for i in range(n):
        b = np.searchsorted(lis, c[i], side='left')
        lis[b] = c[i]

    ans = n - np.searchsorted(lis, np.inf, side='left')
    print(ans)

if __name__ == '__main__':
    main()

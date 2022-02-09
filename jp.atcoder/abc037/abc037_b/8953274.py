import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, q = I[:2]
lrt = I[2:].reshape(-1, 3)


def main():
    res = np.zeros(n, dtype=np.int64)
    for l, r, t in lrt:
        res[l-1:r] = t

    return res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')

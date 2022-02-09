import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, m = I[:2]
ab = I[2:2+n*2].reshape(-1, 2)
cd = I[2+n*2:].reshape(-1, 2)

def main():
    res = np.absolute(cd - ab[:, None])
    res = np.sum(res, axis=2)
    ans = np.argmin(res, axis=1) + 1
    return ans

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')

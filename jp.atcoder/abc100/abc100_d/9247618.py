import sys
import numpy as np
from itertools import product

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, m = I[:2]
x, y, z = I[2:].reshape(n, 3).T

def main():
    ans = 0
    for opx, opy, opz in product([1, -1], repeat=3):
        s = opx * x + opy * y + opz * z
        res = np.sort(s)[::-1][:m].sum()
        ans = max(ans, res)

    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

import sys
import numpy as np
from itertools import permutations

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, C = I[:2]
cost = I[2:2+C**2].reshape(C, C)
color = I[2+C**2:].reshape(n, n) - 1

def main():
    mod_3 = (np.arange(1, n+1)[:, None] + np.arange(1, n+1)) % 3
    c0 = np.bincount(color[mod_3 == 0], minlength=C)
    c1 = np.bincount(color[mod_3 == 1], minlength=C)
    c2 = np.bincount(color[mod_3 == 2], minlength=C)

    ans = float('inf')
    for i, j, k in permutations(range(C), 3):
        res = np.sum(c0 * cost[:, i])
        res += np.sum(c1 * cost[:, j])
        res += np.sum(c2 * cost[:, k])
        ans = min(ans, res)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

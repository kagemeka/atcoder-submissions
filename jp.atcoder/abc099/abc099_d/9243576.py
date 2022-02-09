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

    r = np.arange(C)
    s0 = np.sum(cost[:, r] * c0[:, None], axis=0)
    s1 = np.sum(cost[:, r] * c1[:, None], axis=0)
    s2 = np.sum(cost[:, r] * c2[:, None], axis=0)

    ans = float('inf')
    for i, j, k in permutations(range(C), 3):
        res = s0[i] + s1[j] + s2[k]
        ans = min(ans, res)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

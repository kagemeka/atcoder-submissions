import sys
import numpy as np

n, k, *t = map(int, sys.stdin.read().split())
t = np.array(t, dtype=np.int8).reshape(n, k)

def main():
    res = np.array([0], dtype=np.int8)
    for i in range(n):
        res = res.reshape(-1, 1) ^ t[i]
    ans = 'Found' if np.any(res == 0) else 'Nothing'
    print(ans)

if __name__ ==  '__main__':
    main()

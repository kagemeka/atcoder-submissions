import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, k = I[:2]
t = I[2:].reshape(n, k)

def main():
    res1 = set(t[0])
    for i in range(1, n):
        res2 = set()
        for j in res1:
            res2 |= set(j ^ t[i])
        res1 = res2

    return 'Found' if 0 in res1 else 'Nothing'

if __name__ == '__main__':
    ans = main()
    print(ans)

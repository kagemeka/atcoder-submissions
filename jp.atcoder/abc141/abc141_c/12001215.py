import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int32)
n, k, q = I[:3]; a = I[3:] - 1

def main():
    res = np.full(n, k, dtype=np.int32) - q
    res += np.bincount(a, minlength=n)
    ans = np.full(n, 'No', dtype='U3')
    ans[res > 0] = 'Yes'
    print(*ans, sep='\n')

if __name__ ==  '__main__':
    main()

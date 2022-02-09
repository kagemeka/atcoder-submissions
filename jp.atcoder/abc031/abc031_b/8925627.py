import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
L, H, n = I[:3]
a = I[3:]

def main():
    res = np.zeros(n, dtype=np.int64)
    res = np.maximum(L - a, 0)
    res[a > H] = -1
    return res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')

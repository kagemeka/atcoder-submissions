import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
a = I[1:]

def main():
    c = np.bincount(a)
    res = np.maximum(c - 1, 0)
    ans = np.sum(res)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

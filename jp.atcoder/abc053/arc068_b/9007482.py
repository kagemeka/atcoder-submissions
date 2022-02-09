import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
a = I[1:]

def main():
    res = np.bincount(a)
    ans = np.count_nonzero(res)
    res = np.maximum(0, res - 1)
    ans -= (np.sum(res) & 1)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

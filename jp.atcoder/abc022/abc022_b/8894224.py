import sys
from collections import Counter
import numpy as np

n, *a = map(int, sys.stdin.read().split())

def main():
    c = np.bincount(a)
    res = np.maximum(c - 1, 0)
    ans = np.sum(res)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

import sys
from collections import Counter
import numpy as np

n, *s = sys.stdin.read().split()
n = int(n)

def comb_2(n):
    return n * (n - 1) // 2

def main():
    t = [''.join(sorted(t)) for t in s]
    v = np.array(list(Counter(t).values()), dtype=np.int64)
    return np.sum(comb_2(v))

if __name__ == '__main__':
    ans = main()
    print(ans)

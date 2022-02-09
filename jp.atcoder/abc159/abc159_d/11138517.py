import sys
import numpy as np

def comb(n):
    return n * (n - 1) // 2

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n = I[0]
a = I[1:]

def main():
    c = np.bincount(a, minlength=np.amax(a)+1)
    tot = comb(c).sum()
    res = tot - comb(c[a]) + comb(c[a]-1)
    return res

if __name__ == "__main__":
    ans = main()
    print(*ans, sep='\n')

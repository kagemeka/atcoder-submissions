import sys
import numpy as np

n, l = map(int, sys.stdin.readline().split())

def main():
    f = l + np.arange(1, n+1) - 1
    s = f.sum()
    a = np.absolute(f)
    mi = np.amin(a)
    i = np.argwhere(a == mi)[0, 0]
    return s - f[i]

if __name__ == '__main__':
    ans = main()
    print(ans)

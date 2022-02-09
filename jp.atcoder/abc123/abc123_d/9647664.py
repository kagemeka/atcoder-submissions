import sys
import numpy as np

x, y, z, k = map(int, sys.stdin.readline().split())
a, b, c = (np.array(sys.stdin.readline().split(), dtype=np.int64) for _ in range(3))

def main():
    res = np.sort(np.ravel(a[:, None] + b))[::-1]
    res = np.sort(np.ravel(c[:, None] + res[:min(k, x*y)]))[::-1]
    return res[:k]

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')

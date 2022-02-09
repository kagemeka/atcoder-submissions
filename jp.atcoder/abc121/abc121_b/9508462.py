import sys
import numpy as np

n, m, c = map(int, sys.stdin.readline().split())
b = np.array(sys.stdin.readline().split(), dtype=np.int64)
a = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(n, m)

def main():
    res = np.sum(a * b, axis=1) + c
    return np.count_nonzero(res > 0)

if __name__ == '__main__':
    ans = main()
    print(ans)

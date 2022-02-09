import sys
import numpy as np

n, h, a, b, c, d, e = map(int, sys.stdin.read().split())

def cost(x, y):
    return a * x + c * y

def main():
    x = np.arange(n+1, dtype=np.int64)
    y = (1 + n * e - (b + e) * x - h + (d + e) - 1) // (d + e)
    y = np.maximum(np.minimum(y, n - x), 0)

    return np.amin(cost(x, y))

if __name__ == '__main__':
    ans = main()
    print(ans)

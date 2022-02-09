import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, k = I[:2]
x = I[2:]

def main():
    d = np.minimum(x, k - x)
    return np.sum(d) * 2

if __name__ == '__main__':
    ans = main()
    print(ans)

import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n = I[0]
v, c = I[1:].reshape(2, n)

def main():
    return np.sum(np.maximum(v - c, 0))

if __name__ == '__main__':
    ans = main()
    print(ans)

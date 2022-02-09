import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, d, x = I[:3]
a = I[3:]

def main():
    return x + np.sum((d - 1) // a + 1)

if __name__ == '__main__':
    ans = main()
    print(ans)

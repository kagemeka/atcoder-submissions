import sys
import numpy as np

a, b = np.array(sys.stdin.read().split(), dtype=np.int64)[1:].reshape(2, -1)
np.cumsum(a, out=a)
b = np.cumsum(b[::-1])[::-1]

def main():
    print(np.amax(a + b))

if __name__ ==  '__main__':
    main()

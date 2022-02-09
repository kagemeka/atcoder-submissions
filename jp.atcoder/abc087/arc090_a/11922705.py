import sys
import numpy as np

a = np.array(sys.stdin.read().split(), dtype=np.int64)[1:].reshape(2, -1)

def main():
    np.cumsum(a[0], out=a[0])
    np.cumsum(a[1, ::-1], out=a[1, ::-1])
    print(np.amax(a.sum(axis=0)))

if __name__ ==  '__main__':
    main()

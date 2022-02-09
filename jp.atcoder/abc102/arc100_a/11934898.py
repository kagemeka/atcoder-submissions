import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
a = np.array(sys.stdin.readline().split(), dtype=np.int64)
a -= np.arange(1, n + 1)
a.sort()

def main():
    b = a[n//2]
    print(np.absolute(a - b).sum())

if __name__ ==  '__main__':
    main()

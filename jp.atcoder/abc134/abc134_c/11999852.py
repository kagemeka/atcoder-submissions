import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
a = np.array(sys.stdin.read().split(), dtype=np.int32)
b = np.sort(a.copy())[::-1]

def main():
    bl = a == b[0]
    a[bl], a[~bl] = b[1], b[0]
    print(*a, sep='\n')

if __name__ ==  '__main__':
    main()

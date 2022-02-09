import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
a = np.array(sys.stdin.readline().split(), dtype=np.int64)

def main():
    tmp = np.absolute(a)
    if np.count_nonzero(a) != n:
        return tmp.sum()
    else:
        if np.count_nonzero(a < 0) & 1:
            return tmp.sum() - np.amin(tmp) * 2
        else:
            return tmp.sum()

if __name__ == '__main__':
    ans = main()
    print(ans)

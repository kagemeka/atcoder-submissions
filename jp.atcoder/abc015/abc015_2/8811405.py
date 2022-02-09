import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n = I[0]
a = I[1:]

def main():
    targets = a[np.nonzero(a)]
    l = targets.size
    res = (np.sum(targets) + l - 1) // l
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)

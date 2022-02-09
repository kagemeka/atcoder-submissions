import sys
import numpy as np

n, *a = map(int, sys.stdin.read().split())
a = np.array([0] + a + [0])

def main():
    res1 = np.absolute(a[2:] - a[1:-1]) + np.absolute(a[1:-1] - a[:-2])
    res2 = np.absolute(a[2:] - a[:-2])
    default = np.absolute(a[1:] - a[:-1]).sum()

    ans = default - (res1 - res2)
    return ans

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')

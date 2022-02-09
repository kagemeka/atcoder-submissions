import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
l, r = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(n, 2).T

def main():

    return np.sum(r - l + 1)

if __name__ == '__main__':
    ans = main()
    print(ans)

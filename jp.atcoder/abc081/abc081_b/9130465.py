import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
a = np.array(sys.stdin.readline().split(), dtype=np.int64)

def main(a):
    cnt = 0
    while True:
        if np.any(a & 1):
            return cnt
        a //= 2
        cnt += 1

if __name__ == '__main__':
    ans = main(a)
    print(ans)

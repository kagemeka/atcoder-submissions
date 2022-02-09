import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
a = np.array(sys.stdin.readline().split(), dtype=np.int64)

def main():
    res = np.bincount(np.minimum(a // 400, 8), minlength=9)

    ans_min = np.count_nonzero(res[:8])
    ans_max = ans_min + res[8]
    if ans_min == 0:
        ans_min = 1

    return ans_min, ans_max

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')

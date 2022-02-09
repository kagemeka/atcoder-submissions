import sys
import numpy as np

se = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(-1, 2).T

def main():
    res = np.sum(se[0] * se[1] // 10)
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)

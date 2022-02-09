import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, k = I[:2]
a = I[2:]

def main():
    s = np.cumsum(a)
    res = s[k:] - s[:n-k]
    ans = np.sum(res) + s[k-1]
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

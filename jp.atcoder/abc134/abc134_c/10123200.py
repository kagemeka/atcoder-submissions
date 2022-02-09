import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
a = np.array(sys.stdin.read().split(), dtype=np.int64)

def main():
    b = np.sort(a)
    m1 = b[-1]
    m2 = b[-2]
    res = np.zeros(n, dtype=np.int64)
    res[a <= m2] = m1
    res[res == 0] = m2
    return res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')

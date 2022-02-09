import sys
from math import floor, sqrt

def main():
    n = int(sys.stdin.readline().rstrip())
    m = floor(sqrt(2 * n))
    if m * (m + 1) // 2 < n:
        m += 1
    M = m + 1

    needless = M * (M - 1) // 2 - n

    res = sorted(set(range(1, m + 1)) - set([needless]))
    print(*res, sep='\n')

if __name__ == '__main__':
    main()

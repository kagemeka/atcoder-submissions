import sys
from math import log2, ceil

n, k = map(int, sys.stdin.readline().split())

def main():
    res = 0
    for i in range(1, n+1):
        if i >= k:
            res += n - i + 1
            break
        res += pow(2, -ceil(log2(k / i)))

    return res / n

if __name__ == '__main__':
    ans = main()
    print(ans)

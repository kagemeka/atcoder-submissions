import sys
from bisect import bisect_left as bi_l

n, m, x, *a = map(int, sys.stdin.read().split())

def main():
    left = bi_l(a, x)
    right = m - left
    return min(left, right)

if __name__ == '__main__':
    ans = main()
    print(ans)

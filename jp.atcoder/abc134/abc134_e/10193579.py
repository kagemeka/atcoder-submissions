import sys
from bisect import bisect_right as bi_r

inf = float('inf')

n, *A = map(int, sys.stdin.read().split())

def main():
    res = [inf] * n
    for a in A[::-1]:
        i = bi_r(res, a)
        res[i] = a

    for i in range(n):
        if res[i] == inf:
            return i
    return n

if __name__ == '__main__':
    ans = main()
    print(ans)

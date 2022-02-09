# 2019-11-22 19:20:59(JST)
import sys
from bisect import bisect_left as bi_l


def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    X, Y = [int(x) for x in sys.stdin.readline().split()]

    a = [int(x) for x in sys.stdin.readline().split()] # n
    b = [int(x) for x in sys.stdin.readline().split()] # m

    t = 0
    count = 0 # if count % 2 == 0, a
    while True:
        if count % 2 == 0:
            i = bi_l(a, t)
            if i == n: # no plane
                break
            else: # take plane
                count += 1
                t = a[i] + X
        else:
            j = bi_l(b, t)
            if j == m:
                break
            else:
                count += 1
                t = b[j] + Y

    ans = count // 2
    print(ans)

if __name__ == '__main__':
    main()

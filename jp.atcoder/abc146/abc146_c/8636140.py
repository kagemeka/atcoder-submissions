# 2019-11-24 20:59:47(JST)
import sys
# import numpy as np


def main():
    A, B, X = map(int, sys.stdin.readline().split())


    def cost(n):
        return A * n + B * len(str(n))
    l = 1; r = 10 ** 9
    while l <= r:
        mid = (l + r) // 2
        if cost(mid) == X:
            ans = mid
            break
        elif cost(mid) > X:
            r = mid - 1
        else:
            l = mid + 1

    else:
        ans = r

    print(ans)

if __name__ == '__main__':
    main()

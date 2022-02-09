# 2019-11-22 16:25:33(JST)
import sys


def main():
    n, a, b = [int(x) for x in sys.stdin.readline().split()]


    if a > b:
        ans = 0
    elif a == b:
        ans = 1
    elif b < a:
        if n == 1:
            ans = 0
        else:
            min_possible = a * (n - 1) + b
            max_possible = b * (n - 1) + a
            ans = max_possible - min_possible + 1

    print(ans)

if __name__ == '__main__':
    main()

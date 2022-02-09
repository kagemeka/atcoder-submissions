# 2019-11-22 16:25:33(JST)
import sys


def main():
    n, a, b = [int(x) for x in sys.stdin.readline().split()]

    min_possible = a * (n - 1) + b
    max_possible = b * (n - 1) + a

    ans = max_possible - min_possible + 1
    print(max(ans, 0))

if __name__ == '__main__':
    main()

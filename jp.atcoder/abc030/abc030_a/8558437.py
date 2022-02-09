# 2019-11-22 19:20:59(JST)
import sys


def main():
    a, b, c, d = [int(x) for x in sys.stdin.readline().split()]
    takahashi_p = b / a
    aoki_p = d / c

    if takahashi_p == aoki_p:
        ans = 'DRAW'
    elif takahashi_p > aoki_p:
        ans = 'TAKAHASHI'
    elif takahashi_p < aoki_p:
        ans = 'AOKI'

    print(ans)


if __name__ == '__main__':
    main()

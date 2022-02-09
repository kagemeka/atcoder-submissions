# 2019-11-22 22:30:40(JST)
import sys

def main():
    l = map(int, sys.stdin.read().split())

    ans = 0
    for se in zip(l, l):
        s, e = se[0], se[1]
        ans += s * e // 10

    print(ans)

if __name__ == '__main__':
    main()

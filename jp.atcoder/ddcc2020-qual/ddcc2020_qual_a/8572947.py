# 2019-11-23 21:00:35(JST)
import sys

def main():
    xy = map(int, sys.stdin.readline().split())
    ans = 0
    for i in xy:
        if i == 1:
            ans += 3 * 10 ** 5
        if i == 2:
            ans += 2 * 10 ** 5
        elif i == 3:
            ans += 1 * 10 ** 5

    if ans == 6 * 10 ** 5:
        ans = 1 * 10 ** 6

    print(ans)

if __name__ == '__main__':
    main()

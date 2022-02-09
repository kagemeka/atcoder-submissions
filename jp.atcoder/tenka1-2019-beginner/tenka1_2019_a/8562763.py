# 2019-11-23 01:28:44(JST)
import sys


def main():
    a, b, c = map(int, sys.stdin.readline().split())
    if a < c < b or a > c > b:
        ans = 'Yes'
    else:
        ans = 'No'

    print(ans)

if __name__ == '__main__':
    main()

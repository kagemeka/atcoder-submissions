# 2019-11-22 16:25:33(JST)
import sys


def main():
    s = '.' + sys.stdin.readline().rstrip()
    n = len(s) - 1

    count = 0
    for i in range(1, n+1):
        if s[i] == 'U':
            count += 1 * (n - i) + 2 * (i - 1)
        elif s[i] == 'D':
            count += 1 * (i - 1) + 2 * (n - i)

    print(count)

if __name__ == '__main__':
    main()

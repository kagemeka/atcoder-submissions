# 2019-11-23 01:28:44(JST)
import sys

def main():
    n, s, k = sys.stdin.read().split()
    n, k = map(int, [n, k])

    c = s[k-1]
    letters = set(s) - set(c)
    for l in letters:
        s = s.replace(l, '*')

    print(s)


if __name__ == '__main__':
    main()

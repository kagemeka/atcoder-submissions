# 2019-11-23 01:28:44(JST)
import sys
from string import ascii_lowercase as alphabet


def main():
    n, s, k = sys.stdin.read().split()
    n, k = map(int, [n, k])

    c = s[k-1]
    for l in alphabet:
        if l != c:
            s = s.replace(l, '*')

    print(s)


if __name__ == '__main__':
    main()

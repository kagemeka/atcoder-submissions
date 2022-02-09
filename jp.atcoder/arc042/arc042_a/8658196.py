# 2019-11-26 14:51:37(JST)
import sys

def main():
    n, m, *a = map(int, sys.stdin.read().split())

    res = sorted(set(a), key=list(reversed(a)).index) + sorted(set(range(1, n+1)) - set(a))

    print('\n'.join(map(str, res)))

if __name__ == '__main__':
    main()

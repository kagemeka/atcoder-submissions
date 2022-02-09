import sys
from math import ceil

def main():
    T1, T2, A1, A2, B1, B2 = map(int, sys.stdin.read().split())

    BA1 = A1 - B1
    BA2 = A2 - B2

    if BA1 == 0:
        print(0)
        sys.exit()

    if BA1 < 0:
        BA1 = -BA1
        BA2 = -BA2

    d = BA1 * T1 + BA2 * T2

    if d > 0:
        print(0)
        sys.exit()
    if d == 0:
        print('infinity')
        sys.exit()

    # dは負なので
    n = ceil((- BA1 * T1) / d)
    if n * d + BA1 * T1 == 0:
        ans = n * 2
    else:
        ans = n * 2 - 1

    print(ans)

if __name__ == '__main__':
    main()

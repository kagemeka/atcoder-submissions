# 2019-11-23 01:09:31(JST)
import sys
import itertools



def main():
    n, *a = map(int, sys.stdin.read().split())
    a.sort()

    b = list(itertools.accumulate(a))

    count = 1
    for i in range(n-1, 0, -1):
        if a[i] <= b[i-1] * 2:
            count += 1
        else:
            break

    print(count)

if __name__ == '__main__':
    main()

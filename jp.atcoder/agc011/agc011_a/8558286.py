# 2019-11-22 16:56:24(JST)
import sys


def main():
    n, c, k, *T = [int(x) for x in sys.stdin.read().split()]
    T.sort()


    count = 0
    bus_count = 1
    t = T[0]
    for i in range(n):
        if T[i] - t > k:
            bus_count += 1
            count = 1
            t = T[i]
            continue
        count += 1
        if count > c:
            bus_count += 1
            count = 1
            t = T[i]

    print(bus_count)


if __name__ == '__main__':
    main()

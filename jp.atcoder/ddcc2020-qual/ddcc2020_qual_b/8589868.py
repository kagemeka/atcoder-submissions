import sys

def main():
    n, *a = map(int, sys.stdin.readline().split())

    l = 0
    r = sum(a)
    m = sum(a)
    for i in range(n):
        l += a[i]
        r -= a[i]
        m = min(m, abs(l - r))

    print(m)


if __name__ == '__main__':
    main()

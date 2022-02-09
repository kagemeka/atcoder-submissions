import sys

n, *a = map(int, sys.stdin.read().split())
a.sort()

def main():
    m = n // 2
    l, r = a[m-1], a[m]
    print(r - l)

if __name__ ==  '__main__':
    main()

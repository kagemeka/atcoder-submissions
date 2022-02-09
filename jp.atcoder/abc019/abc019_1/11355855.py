import sys

*a, = map(int, sys.stdin.readline().split())
a.sort()

def main():
    print(a[1])

if __name__ ==  '__main__':
    main()

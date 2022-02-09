import sys

n, *cap = map(int, sys.stdin.read().split())
m = min(cap)

def main():
    print((n + m - 1) // m + 4)

if __name__ ==  '__main__':
    main()

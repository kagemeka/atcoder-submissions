import sys

n, k = map(int, sys.stdin.readline().split())

def main():
    print((n + k - 3) // (k - 1))

if __name__ ==  '__main__':
    main()

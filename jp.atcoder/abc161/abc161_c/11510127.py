import sys

n, k = map(int, sys.stdin.readline().split())

def main():
    r = n % k
    print(min(r, k - r))

if __name__ ==  '__main__':
    main()

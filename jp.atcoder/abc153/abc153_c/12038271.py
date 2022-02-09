import sys

n, k, *h = map(int, sys.stdin.read().split())

def main():
    print(sum(sorted(h)[:n-k]))

if __name__ ==  '__main__':
    main()

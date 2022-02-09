import sys

n, k, *h = map(int, sys.stdin.read().split())

def main():
    print(sum(sorted(h)[:max(0, n-k)]))
    print(sum([]))

if __name__ ==  '__main__':
    main()

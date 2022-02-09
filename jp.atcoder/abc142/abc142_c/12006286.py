import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    res = [x[0] for x in sorted(enumerate(a, 1), key=lambda x: x[1])]
    print(*res, sep=' ')

if __name__ ==  '__main__':
    main()

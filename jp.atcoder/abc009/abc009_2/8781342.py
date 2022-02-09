import sys

n, *c = map(int, sys.stdin.read().split())
c = sorted(set(c))

def main():
    print(c[-2])

if __name__ == '__main__':
    main()

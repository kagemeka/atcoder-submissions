import sys

n, m, *a = map(int, sys.stdin.read().split())

def main():
    r = n - sum(a)
    print(r if r >= 0 else -1)

if __name__ == '__main__':
    main()

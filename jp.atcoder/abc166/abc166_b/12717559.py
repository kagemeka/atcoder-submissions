import sys

n, k = map(int, sys.stdin.readline().split())

def main():
    res = set()
    for _ in range(k):
        d = int(sys.stdin.readline().rstrip())
        *a, = map(int, sys.stdin.readline().split())
        res |= set(a)
    print(n - len(res))

if __name__ == '__main__':
    main()

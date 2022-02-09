import sys

n, k, x, y = map(int, sys.stdin.read().split())

def main():
    if n <= k:
        res = x * n
    else:
        res = x * k + y * (n - k)
    print(res)

if __name__ ==  '__main__':
    main()

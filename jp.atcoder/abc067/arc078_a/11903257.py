import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    for i in range(n - 1): a[i+1] += a[i]
    res = float('inf')
    for i in range(n - 1): res = min(res, abs(a[-1] - a[i] * 2))
    print(res)

if __name__ ==  '__main__':
    main()

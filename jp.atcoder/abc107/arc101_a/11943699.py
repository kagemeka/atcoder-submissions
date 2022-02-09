import sys

n, k, *x = map(int, sys.stdin.read().split())

def main():
    res = float('inf')
    for i in range(n - k + 1):
        j = i + k - 1
        if x[i] < 0:
            d = -x[i] if x[j] <= 0 else min(-x[i], x[j]) * 2 + max(-x[i], x[j])
        else:
            d = x[j]
        res = min(res, d)
    print(res)

if __name__ ==  '__main__':
    main()

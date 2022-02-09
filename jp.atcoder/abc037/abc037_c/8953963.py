import sys

n, k, *a = map(int, sys.stdin.read().split())

def main():
    res = 0
    if n >= k * 2:
        for i in range(n):
            if i + 1 < k:
                res += a[i] * (i + 1)
            elif n - i < k:
                res += a[i] * (n - i)
            else:
                res += a[i] * k

    else:
        for i in range(n // 2):
            res += a[i] * (i + 1)
        for i in range(n // 2, n):
            res += a[i] * (n - i)

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)

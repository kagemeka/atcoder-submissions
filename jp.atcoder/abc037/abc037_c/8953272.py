import sys

n, k, *a = map(int, sys.stdin.read().split())
a = [None] + a

def main():
    res = 0
    for i in range(1, n+1):
        if i < k:
            res += a[i] * i
        elif n - i + 1 < k:
            res += a[i] * (n - i + 1)
        else:
            res += a[i] * k

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)

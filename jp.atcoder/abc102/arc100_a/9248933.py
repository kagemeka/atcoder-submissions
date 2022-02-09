import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    for i in range(n):
        a[i] -= (i + 1)
    a.sort()
    b = a[n // 2]
    res = 0
    for i in range(n):
        res += abs(a[i] - b)

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)

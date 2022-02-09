import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    x = 0
    y = sum(a)
    res = []
    for i in range(n-1):
        x += a[i]
        y -= a[i]
        res.append(abs(x - y))

    return min(res)

if __name__ == '__main__':
    ans = main()
    print(ans)

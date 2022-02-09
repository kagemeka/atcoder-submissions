import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    res = -10 ** 3
    for i in range(n):
        ao = -10 ** 3
        for j in range(i):
            taka = sum(a[j:i+1:2])
            aoki = sum(a[j+1:i+1:2])
            if aoki > ao:
                ao = aoki
                ta = taka
        for j in range(i+1, n):
            taka = sum(a[i:j+1:2])
            aoki = sum(a[i+1:j+1:2])
            if aoki > ao:
                ao = aoki
                ta = taka

        res = max(res, ta)

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)

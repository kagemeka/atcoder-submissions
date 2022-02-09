import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    res = 0
    for i in range(1, n-1):
        cur = a[i]
        l = 0
        for j in range(i):
            if a[j] < cur:
                l += 1
        r = 0
        for j in range(i+1, n):
            if a[j] < cur:
                r += 1
        res += l * r

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)

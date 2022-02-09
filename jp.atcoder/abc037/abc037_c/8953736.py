import sys

n, k, *a = map(int, sys.stdin.read().split())

def main():
    res = 0
    l = 0
    r = k
    s = sum(a[l:r])
    res += s
    for _ in range(n-k):
        s -= a[l]
        l += 1
        s += a[r]
        r += 1
        res += s

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)

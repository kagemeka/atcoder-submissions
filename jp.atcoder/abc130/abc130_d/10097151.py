import sys

n, k, *a = map(int, sys.stdin.read().split())

def main():
    s = 0
    l = r = 0
    cnt = 0
    while r <= n:
        if s >= k:
            cnt += n - (r - 1)
            s -= a[l]
            l += 1
        else:
            if r == n:
                break
            s += a[r]
            r += 1
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)

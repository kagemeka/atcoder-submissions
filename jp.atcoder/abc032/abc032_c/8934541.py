import sys

n, k, *s = map(int, sys.stdin.read().split())

def main():
    if 0 in s:
        return n

    res = [0] * n
    l = 0
    r = 0
    cumprod = s[0]
    while True:
        if cumprod <= k:
            res[l] = r - l + 1
            r += 1
            if r == n :
                break
            cumprod *= s[r]
        else:
            res[l] = r - l
            cumprod //= s[l]
            l += 1
            if l > r:
                r += 1
                if r == n:
                    break
                cumprod *= s[r]

    ans = max(res)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

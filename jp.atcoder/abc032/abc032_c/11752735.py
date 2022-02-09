import sys

n, k, *a = map(int, sys.stdin.read().split())

def main():
    a.append(k + 1)
    for x in a:
        if x == 0:
            print(n)
            return
    l = 0
    tmp = 1
    res = 0
    for r in range(n + 1):
        tmp *= a[r]
        if tmp > k:
            res = max(res, r - l)
            while tmp > k:
                tmp //= a[l]
                l += 1
                if l > r:
                    break
    print(res)

if __name__ ==  '__main__':
    main()

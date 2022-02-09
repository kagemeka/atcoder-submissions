import sys

n, *a = map(int, sys.stdin.read().split())

cumsum = [0] + a
cumxor = cumsum.copy()
for i in range(1, n):
    cumsum[i+1] += cumsum[i]
    cumxor[i+1] ^= cumxor[i]

def is_ok(l, r):
    s = cumsum[r] - cumsum[l-1]
    x = cumxor[r] ^ cumxor[l-1]
    return s == x

def main():
    res = 0
    for l in range(1, n+1):
        lo = l - 1; hi = n+1
        while lo + 1 < hi:
            r = (lo + hi) // 2
            if is_ok(l, r):
                lo = r
            else:
                hi = r
        res += lo - l + 1

    return res
if __name__ == '__main__':
    ans = main()
    print(ans)

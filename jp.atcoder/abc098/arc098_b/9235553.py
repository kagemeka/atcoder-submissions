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
    l = r = 1
    flag = False
    while l <= n and r <= n:
        if is_ok(l, r):
            if r == n:
                res += r - l + 1
                l += 1
                flag = False
            else:
                flag = True
                r += 1
        else:
            if flag:
                res += r - 1 - l + 1
            else:
                res += r - l + 1
            l += 1
    return res
if __name__ == '__main__':
    ans = main()
    print(ans)

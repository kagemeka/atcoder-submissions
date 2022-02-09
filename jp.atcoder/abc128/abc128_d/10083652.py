import sys

n, k, *v = map(int, sys.stdin.read().split())

def main():
    m = min(n, k)
    res = 0
    for i in range(m+1):
        for j in range((m-i)+1):
            l = v[:i]
            r = v[-j:] if j > 0 else []
            take = l + r
            s = sum(take)
            neg = [t for t in take if t < 0]
            neg.sort()
            s -= sum(neg[:(k-(i+j))])
            res = max(res, s)
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)

import sys

n, k, *v = map(int, sys.stdin.read().split())

def main():
    m = min(n, k)
    ans = 0
    for i in range(m+1):
        for j in range((m-i)+1):
            tmp = v[:i] + v[-j:] if j else v[:i]

            res = sum(tmp) if tmp else 0
            neg = [t for t in tmp if t < 0]
            neg.sort()
            res -= sum(neg[:m-(i+j)])
            ans = max(ans, res)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

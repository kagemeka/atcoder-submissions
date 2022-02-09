import sys

n, k = map(int, sys.stdin.readline().split())

def main():
    res = 0
    for b in range(k+1, n+1):
        q, r = divmod(n, b)
        res += q * (b - k) + max(0, r - (k - 1))
    if k == 0:
        res -= n - k
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)

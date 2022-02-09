import sys

n, k = map(int, sys.stdin.readline().split())

def main():
    res = 0
    for b in range(k+1, n+1):
        q, r = divmod(n, b)
        res += q * (b - k) + max(0, r - (max(k, 1) - 1))
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)

import sys

n, p = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().rstrip()

def main():
    dp = [0] * p
    res = 0
    for d in s:
        d = int(d)
        nex = [0] * p
        for i in range(p):
            nex[(i*10+d)%p] += dp[i]
        nex[d%p] += 1
        dp = nex
        res += dp[0]
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)

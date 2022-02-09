import sys

n, k, c = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().rstrip()

def make(s):
    dp = [[0] * 2 for _ in range(n + 2)]
    for i in range(n):
        dp[i+1][0] = max(dp[i][0], dp[i][1])
        if s[i] == 'o':
            if i + 1 - c < 0:
                dp[i+1][1] = 1
            else:
                dp[i+1][1] = dp[i+1-c][0] + 1
    return dp

def main():
    dp_l = make(s)
    dp_r = make(s[::-1])[::-1]

    for i in range(1, n + 1):
        if s[i-1] == 'o':
            if dp_l[i][0] + dp_r[i][0] < k:
                print(i)

if __name__ ==  '__main__':
    main()

import sys

n = sys.stdin.readline().rstrip()

def main():
    dp = [0, 1]
    for d in n:
        d = int(d)
        dp[0], dp[1] = min(dp[0]+d, dp[1]+10-d), min(dp[0]+d+1, dp[1]+10-d-1)

    return dp[0]

if __name__ == '__main__':
    ans = main()
    print(ans)

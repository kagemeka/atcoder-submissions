import sys

inf = float('inf')

h, n, *ab = map(int, sys.stdin.read().split())
ab = list(zip(*[iter(ab)] * 2))

def main():
    dp = [inf] * (h + 1)
    dp[0] = 0
    for i in range(1, h+1):
        for a, b in ab:
            dp[i] = min(dp[i], dp[max(i-a, 0)] + b)

    return dp[h]

if __name__ == '__main__':
    ans = main()
    print(ans)

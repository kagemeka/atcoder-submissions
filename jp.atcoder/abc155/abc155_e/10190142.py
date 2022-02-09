import sys

n = sys.stdin.readline().rstrip()
l = len(n)

def main():
    dp0 = [None] * (l + 1)
    dp1 = [None] * (l + 1)
    dp0[0] = 0
    dp1[0] = 1

    for i in range(l):
        d = int(n[i])
        dp0[i+1] = min(dp0[i]+d, dp1[i]+10-d)
        dp1[i+1] = min(dp0[i]+d+1, dp1[i]+10-d-1)

    return dp0[l]

if __name__ == '__main__':
    ans = main()
    print(ans)

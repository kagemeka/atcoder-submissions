import sys

MOD = 10 ** 9 + 7

s = sys.stdin.readline().rstrip()
l = len(s)

def main():
    dp1 = [0] * (l + 1)
    dp2 = [0] * (l + 1)
    dp2[0] = 1
    for i in range(l):
        dp1[i+1] += dp1[i] * 3
        if s[i] == '1':
            dp1[i+1] += dp2[i]
            dp2[i+1] += dp2[i] * 2
        else:
            dp2[i+1] += dp2[i]
    dp1[i+1] %= MOD
    dp2[i+1] %= MOD

    return dp1[l] + dp2[l]

if __name__ == '__main__':
    ans = main()
    print(ans)

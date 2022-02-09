import sys

MOD = 2019

l, r = map(int, sys.stdin.readline().split())

def main():
    if r - l >= MOD - 1:
        return 0
    lm = l % MOD
    rm = r % MOD
    if lm == 0 or lm > rm:
        return 0
    else:
        res = MOD - 1
        for i in range(l, r):
            for j in range(i+1, r+1):
                res = min(res, i % MOD * j % MOD)
        return res

if __name__ == '__main__':
    ans = main()
    print(ans)

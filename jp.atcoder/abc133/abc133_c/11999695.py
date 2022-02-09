import sys
MOD = 2019

l, r = map(int, sys.stdin.readline().split())
r = min(r, l + MOD - 1)

def main():
    res = MOD - 1
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            res = min(res, (i % MOD) * (j % MOD) % MOD)
    print(res)

if __name__ ==  '__main__':
    main()

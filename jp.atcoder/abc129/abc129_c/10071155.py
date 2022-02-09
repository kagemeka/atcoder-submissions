import sys

MOD = 10 ** 9 + 7

n, m, *a = map(int, sys.stdin.read().split())
broken = set(a)

def main():
    res = [None] * (n + 1)
    res[0] = 1
    res[1] = 0 if 1 in broken else 1

    for i in range(2, n+1):
        if i in broken:
            res[i] = 0
        else:
            res[i] = res[i-2] + res[i-1]
            res[i] %= MOD

    return res[n]

if __name__ == '__main__':
    ans = main()
    print(ans)

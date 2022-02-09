import sys
MOD = 10 ** 9 + 7

n, m, *broken = map(int, sys.stdin.read().split())
broken = set(broken)

def main():
    ways = [0] * (n + 1)
    ways[0] = 1
    ways[1] = not 1 in broken
    for i in range(2, n + 1):
        ways[i] = (not i in broken) * (ways[i-1] + ways[i-2]) % MOD
    print(ways[n])

if __name__ ==  '__main__':
    main()

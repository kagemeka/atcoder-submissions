import sys

MOD = 10 ** 9 + 7

a, b, c = map(int, sys.stdin.readline().split())

def main():
    return a*b % MOD * c % MOD

if __name__ == '__main__':
    ans = main()
    print(ans)

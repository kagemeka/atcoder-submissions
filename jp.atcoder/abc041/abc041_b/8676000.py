# 2019-11-27 22:34:20(JST)
import sys

MOD = 10 ** 9 + 7
def main():
    a, b, c = map(int, sys.stdin.readline().split())
    ans = (a * b % MOD * c) % MOD
    print(ans)

if __name__ == '__main__':
    main()

import sys

MOD = 10 ** 9 + 7
n = int(sys.stdin.readline().rstrip())

def main():
    res = 1
    for i in range(1, n+1):
        res *= i
        res %= MOD

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)

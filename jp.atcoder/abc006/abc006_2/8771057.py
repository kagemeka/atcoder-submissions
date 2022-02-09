import sys

MOD = 10 ** 4 + 7

tribonacci = [None] * 10 ** 6
tribonacci[0], tribonacci[1], tribonacci[2] = 0, 0, 1
for i in range(3, 10 ** 6):
    tribonacci[i] = sum(tribonacci[i-3:i]) % MOD

n = int(sys.stdin.readline().rstrip())

def main():
    ans = tribonacci[n-1]
    print(ans)

if __name__ == '__main__':
    main()

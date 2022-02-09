import sys

n, y = map(int, sys.stdin.readline().split())
y //= 1000

def main():
    for i in range(n, -1, -1):
        for j in range(n-i, -1, -1):
            k = n - i - j
            if 10*i + 5*j + k == y:
                return i, j, k
    return -1, -1, -1

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')

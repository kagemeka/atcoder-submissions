import sys

a, b, k = map(int, sys.stdin.readline().split())

def main():
    if a >= k:
        return a - k, b
    elif a + b >= k:
        return 0, a + b - k
    else:
        return 0, 0

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')

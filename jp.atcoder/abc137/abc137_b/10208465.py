import sys

k, x = map(int, sys.stdin.readline().split())

def main():
    l = max(-10 ** 6, x - (k - 1))
    r = min(10 ** 6, x + (k - 1))
    return range(l, r + 1)

if __name__ == '__main__':
    ans = main()
    print(*ans, sep =' ')

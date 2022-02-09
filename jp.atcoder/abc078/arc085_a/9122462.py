import sys

n, m = map(int, sys.stdin.readline().split())

def main():
    x = 100 * (n - m) + 1900 * m
    ans = x * 2 ** m
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

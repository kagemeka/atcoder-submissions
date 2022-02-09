import sys

n, k = map(int, sys.stdin.readline().split())

def main():
    return 1 if n % k else 0

if __name__ == '__main__':
    ans = main()
    print(ans)

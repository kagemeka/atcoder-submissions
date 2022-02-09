import sys

d, n = map(int, sys.stdin.readline().split())

def main():
    return 100 ** d * n if n < 100 else 100 ** d * 101

if __name__ == '__main__':
    ans = main()
    print(ans)

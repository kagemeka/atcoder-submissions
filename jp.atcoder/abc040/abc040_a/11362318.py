import sys

n, x = map(int, sys.stdin.readline().split())

def main():
    ans = min(n - x, x - 1)
    print(ans)

if __name__ ==  '__main__':
    main()

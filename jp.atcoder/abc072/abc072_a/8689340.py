import sys

def main():
    X, t = map(int, sys.stdin.readline().split())
    ans = max(0, X - t)
    print(ans)

if __name__ == '__main__':
    main()

import sys

x, y = map(int, sys.stdin.readline().split())

def main():
    ans = y // x
    print(ans)

if __name__ == '__main__':
    main()

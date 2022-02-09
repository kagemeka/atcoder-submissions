import sys

a, b = map(int, sys.stdin.read().split())

def main():
    ans = (a + b - 1) // b * b - a
    print(ans)

if __name__ == '__main__':
    main()

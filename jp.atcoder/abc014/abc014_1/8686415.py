import sys
def main():
    a, b = map(int, sys.stdin.read().split())
    if a % b == 0:
        ans = 0
    else:
        ans = b - a % b
    print(ans)

if __name__ == '__main__':
    main()

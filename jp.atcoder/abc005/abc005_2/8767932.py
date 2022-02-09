import sys
n, *t = map(int, sys.stdin.read().split())

def main():
    ans = min(t)
    print(ans)

if __name__ == '__main__':
    main()

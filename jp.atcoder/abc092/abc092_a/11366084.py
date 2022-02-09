import sys

a, b, c, d = map(int, sys.stdin.read().split())

def main():
    ans = min(a, b) + min(c, d)
    print(ans)

if __name__ ==  '__main__':
    main()

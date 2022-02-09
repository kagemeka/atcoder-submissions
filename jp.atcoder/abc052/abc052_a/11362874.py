import sys

a, b, c, d = map(int, sys.stdin.readline().split())

def main():
    ans = max(a * b, c * d)
    print(ans)

if __name__ ==  '__main__':
    main()

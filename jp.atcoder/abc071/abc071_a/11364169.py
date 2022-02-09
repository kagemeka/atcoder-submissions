import sys

x, a, b = map(int, sys.stdin.readline().split())

def main():
    db = abs(b - x)
    da = abs(a - x)
    ans = 'A' if da < db else 'B'
    print(ans)

if __name__ ==  '__main__':
    main()

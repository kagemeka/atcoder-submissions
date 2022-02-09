import sys

x, a, b = map(int, sys.stdin.readline().split())

def main():
    return 'A' if abs(a - x) < abs(b - x) else 'B'

if __name__ == '__main__':
    ans = main()
    print(ans)

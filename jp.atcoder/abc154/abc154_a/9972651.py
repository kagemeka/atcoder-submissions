import sys

s, t = sys.stdin.readline().split()
a, b = map(int, sys.stdin.readline().split())
u = sys.stdin.readline().rstrip()

def main():
    if u == s:
        return a - 1, b
    else:
        return a, b - 1

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')

import sys

n, m, X, Y = map(int, sys.stdin.readline().split())
*x, = map(int, sys.stdin.readline().split())
*y, = map(int, sys.stdin.readline().split())

def main():
    return 'No War' if max(X, max(x)) < min(Y, min(y)) else 'War'

if __name__ == '__main__':
    ans = main()
    print(ans)

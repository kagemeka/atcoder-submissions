import sys

n, a, b = map(int, sys.stdin.readline().split())

def main():
    ans = min(n * a, b)
    print(ans)

if __name__ ==  '__main__':
    main()

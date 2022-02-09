import sys

n, k = map(int, sys.stdin.readline().split())

def main():
    ans = 1 if n % k else 0
    print(ans)

if __name__ ==  '__main__':
    main()

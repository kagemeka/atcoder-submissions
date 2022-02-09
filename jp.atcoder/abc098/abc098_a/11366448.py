import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    ans = max(a+b, a-b, a*b)
    print(ans)

if __name__ ==  '__main__':
    main()

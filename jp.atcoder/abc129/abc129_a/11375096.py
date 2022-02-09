import sys

*t, = map(int, sys.stdin.readline().split())

def main():
    ans = sum(t) - max(t)
    print(ans)

if __name__ ==  '__main__':
    main()

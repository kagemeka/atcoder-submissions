import sys

*a, = map(int, sys.stdin.readline().split())
a.sort(reverse=True)

def main():
    ans = a[0] * 10 + a[1] + a[2]
    print(ans)

if __name__ ==  '__main__':
    main()

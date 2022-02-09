import sys

*c, = map(int, sys.stdin.readline().split())

def main():
    c.sort()
    ans = 'Yes' if c[0] + c[1] == c[2] else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()

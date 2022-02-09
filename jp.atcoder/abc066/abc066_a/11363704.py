import sys

*c, = map(int, sys.stdin.readline().split())
c.sort()

def main():
    print(c[0] + c[1])

if __name__ ==  '__main__':
    main()

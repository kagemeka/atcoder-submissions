import sys

a, b, c, d, e = map(int, sys.stdin.readline().split())

def main():
    print(max(a + d + e, b + c + e))

if __name__ ==  '__main__':
    main()

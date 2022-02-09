import sys

r, g = map(int, sys.stdin.read().split())

def main():
    res = 2 * g - r
    print(res)

if __name__ ==  '__main__':
    main()

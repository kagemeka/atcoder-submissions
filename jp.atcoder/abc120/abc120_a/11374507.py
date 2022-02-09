import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    res = min(b // a, c)
    print(res)

if __name__ ==  '__main__':
    main()

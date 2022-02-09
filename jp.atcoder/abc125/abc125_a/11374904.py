import sys

a, b, t = map(int, sys.stdin.readline().split())

def main():
    res = b * (t // a)
    print(res)

if __name__ ==  '__main__':
    main()

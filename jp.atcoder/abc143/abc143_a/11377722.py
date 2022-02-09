import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    r = max(0, a - b * 2)
    print(r)

if __name__ ==  '__main__':
    main()

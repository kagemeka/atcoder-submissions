import sys

x, a, b = map(int, sys.stdin.read().split())
x -= a

def main():
    r = x % b
    print(r)

if __name__ ==  '__main__':
    main()

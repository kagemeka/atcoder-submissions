import sys

x, a, b = map(int, sys.stdin.read().split())
x -= a

def main():
    q, r = divmod(x, b)
    print(r)

if __name__ ==  '__main__':
    main()

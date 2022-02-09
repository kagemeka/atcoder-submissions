import sys

a, b, c, x, y = map(int, sys.stdin.readline().split())
if x > y:
    a, b = b, a
    x, y = y, x

def main():
    res = min(c * 2, a + b) * x + min(c * 2, b) * (y - x)
    print(res)

if __name__ ==  '__main__':
    main()

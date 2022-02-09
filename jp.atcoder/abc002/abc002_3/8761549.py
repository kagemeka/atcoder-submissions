import sys

def s(x1, y1, x2, y2):
    return abs(x1 * y2 - y1 * x2) / 2

def main():
    xa, ya, xb, yb, xc, yc = map(int, sys.stdin.readline().split())
    x1 = xb - xa
    x2 = xc - xa
    y1 = yb - ya
    y2 = yc - ya

    print(s(x1, y1, x2, y2))

if __name__ == '__main__':
    main()

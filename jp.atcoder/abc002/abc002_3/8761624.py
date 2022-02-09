import sys

def area(xa, ya, xb, yb, xc, yc):
    x1 = xb - xa
    x2 = xc - xa
    y1 = yb - ya
    y2 = yc - ya
    return abs(x1 * y2 - y1 * x2) / 2

def main():
    xa, ya, xb, yb, xc, yc = map(int, sys.stdin.readline().split())

    print(area(xa, ya, xb, yb, xc, yc))

if __name__ == '__main__':
    main()

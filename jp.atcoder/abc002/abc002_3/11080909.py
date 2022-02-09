import sys

def triangle_area(xa, ya, xb, yb, xc, yc):
    xb -= xa; xc -= xa
    yb -= ya; yc -= ya
    s = abs(xb*yc - xc*yb)/2
    return s

i = map(int, sys.stdin.readline().split())

def main():
    return triangle_area(*i)

if __name__ == '__main__':
    ans = main()
    print(ans)

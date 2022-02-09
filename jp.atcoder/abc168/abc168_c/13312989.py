import sys
from math import cos, sqrt, pi

a, b, h, m = map(int, sys.stdin.readline().split())

def main():
    d = 6 * m
    c = 30 * (h + m / 60)
    theta = abs(d - c)
    ans = sqrt(a ** 2 + b ** 2 - 2*a*b*cos(theta * 2 * pi / 360))
    print(ans)

if __name__ == '__main__':
    main()

import sys
from math import pi, sin

A, B, C = map(int, sys.stdin.readline().split())

def f(t):
    return A*t + B*sin(C*t*pi)

def main():
    l = 0
    r = 200 # 1 <= A, B <= 100 よりどんなに遅くてもt <= 200までに打つ。
    while True:
        t = (l + r) / 2
        x = f(t)
        if abs(x - 100) <= 1e-06:
            return t
        if x > 100:
            r = t
        else:
            l = t

if __name__ == '__main__':
    ans = main()
    print(ans)

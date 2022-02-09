import sys
from math import pi, sin
from scipy.optimize import brentq

A, B, C = map(int, sys.stdin.readline().split())

def f(t):
    return A*t + B*sin(C*t*pi) - 100

def main():
    ans = brentq(f, 0, 200)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

import sys
from math import pi, sin
from scipy.optimize import toms748

A, B, C = map(int, sys.stdin.readline().split())

def f(t):
    return A*t + B*sin(C*t*pi) - 100

def main():
    ans = toms748(f, 0, 200)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

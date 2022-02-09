import sys
from math import sqrt

a, b, c = map(int, sys.stdin.readline().split())

def main():
    d = sqrt(c) - sqrt(a) - sqrt(b)
    # l = 4 * a * b
    # r = (c - a - b) ** 2
    return 'Yes' if d > 0 else 'No'

if __name__ == "__main__":
    ans = main()
    print(ans)

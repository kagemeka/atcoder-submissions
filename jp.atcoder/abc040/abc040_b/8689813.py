import sys
from math import floor, sqrt
def main():
    n = int(sys.stdin.readline().rstrip())

    res = n
    for i in range(1, floor(sqrt(n)) + 1):
        h = i
        w = n // i
        cost = n - h * w + w - h
        res = min(res, cost)

    print(res)
if __name__ == '__main__':
    main()

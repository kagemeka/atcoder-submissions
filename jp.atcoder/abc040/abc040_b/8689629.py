import sys
from math import floor, sqrt
def main():
    n = int(sys.stdin.readline().rstrip())
    h = floor(sqrt(n))
    res1 = n - h ** 2

    h, w = h - 1, h + 2
    while True:
        if n - h * w >= 0:
            res2 = n - w * h + w - h
            break
        else:
            h -= 1
            w += 1

    ans = min(res1, res2)
    print(ans)

if __name__ == '__main__':
    main()

import sys
from itertools import product


def main():
    x1, y1, r, x2, y2, x3, y3 = map(int, sys.stdin.read().split())

    # red
    if x2 <= x1 - r and x3 >= x1 + r and y2 <= y1 - r and y3 >= y1 + r:
        ans_red = 'NO'
    else:
        ans_red = 'YES'

    # blue
    for x, y in product([x2, x3], [y2, y3]):
        d = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
        if d > r:
            ans_blue = 'YES'
            break
    else:
        ans_blue = 'NO'

    print(ans_red)
    print(ans_blue)

if __name__ == '__main__':
    main()

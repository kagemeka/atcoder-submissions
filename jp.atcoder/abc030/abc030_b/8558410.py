# 2019-11-22 19:20:59(JST)
import sys


def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    nn = (n % 12 + m / 60) * 5 * 6
    mm = m * 6
    angle_diff = min(abs(nn - mm), 360 - abs(nn - mm))
    print(angle_diff)

if __name__ == '__main__':
    main()

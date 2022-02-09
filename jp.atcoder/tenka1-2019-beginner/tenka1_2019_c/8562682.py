# 2019-11-23 01:28:44(JST)
import sys


def main():
    n, s = sys.stdin.read().split()
    n = int(n)

    # 各indexを基点として、右側の白の数と左側の黒の数の和の最小値を求めればいい
    black_count = s.count('#')

    left_black = 0
    right_white = n - black_count
    minimum = left_black + right_white
    for i in range(0, n):
        if s[i] == '#':
            left_black += 1
        elif s[i] == '.':
            right_white -= 1
        minimum = min(minimum, left_black + right_white)

    print(minimum)

if __name__ == '__main__':
    main()

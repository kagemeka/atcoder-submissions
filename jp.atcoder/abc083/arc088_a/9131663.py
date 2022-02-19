import sys
from math import floor, log2

x, y = map(int, sys.stdin.readline().split())


def main():
    return 1 + floor(log2(y // x))


if __name__ == "__main__":
    ans = main()
    print(ans)

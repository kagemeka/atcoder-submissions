import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())


def main():
    x3 = x2 + (y1 - y2)
    y3 = y2 - (x1 - x2)
    x4 = x1 + (y1 - y2)
    y4 = y1 - (x1 - x2)
    return x3, y3, x4, y4


if __name__ == "__main__":
    ans = main()
    print(*ans, sep=" ")

import sys
from math import floor, log2

n = int(sys.stdin.readline().rstrip())


def main():
    x = floor(log2(n))
    return 2**x


if __name__ == "__main__":
    ans = main()
    print(ans)

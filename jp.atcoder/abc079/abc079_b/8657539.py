import sys

lucas_nums = [None] * 100


def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    if lucas_nums[n]:
        return lucas_nums[n]
    lucas_nums[n] = lucas(n - 2) + lucas(n - 1)
    return lucas_nums[n]


def main():
    n = int(sys.stdin.readline().rstrip())
    print(lucas(n))


if __name__ == "__main__":
    main()

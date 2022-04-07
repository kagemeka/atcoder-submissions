def main() -> None:
    # |a_i - a_j| <= 1, if not, impossible.
    # if a_i - a_j == 0
    # then both color_i and color_j are unique,
    # or both are belongs to a color group
    # with more than or equal to 2 same color.
    # sum(a_i) is reduced by n - 1 per color duplication.
    # kind of colors can be calculated

    n = int(input())
    a = list(map(int, input().split()))

    # x := number of i such that color_i is unique
    # y := number of colors more than 1
    # sum(a) = (n - 1) * n - y * (n - 2) - (n - x - 2 * y) * (n - 1)

    a.sort()
    if a[-1] - a[0] > 1:
        print("No")
        return

    x = a.count(a[0])
    s = sum(a)
    if x == n:
        if a[0] == n - 1:
            print("Yes")
            return
        x = 0

    if n - x == 1:
        print("No")
        return
    s -= x * (n - 1)
    if s < 0 or s % n != 0:
        print("No")
    else:
        y = s // n
        print("Yes" if y <= (n - x) // 2 else "No")
        # print(x, y)
    # s = -y(n - 2) + x(n - 1) + 2y(n - 1)
    # s = ny + x(n - 1)


if __name__ == "__main__":
    main()

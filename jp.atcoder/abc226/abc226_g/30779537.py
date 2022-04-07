def solve() -> None:
    # person whose strength is i can only carry parcels whose weight is less than or equal to i.

    # check in descending order of degree of freedom of remained parcels.

    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))

    # for i in range(1, 6): # strength
    # 5 -> 4 -> 3 -> 2 -> 1

    if a[5] > b[5]:
        print("No")
        return
    b[5] -= a[5]
    a[5] = 0
    if a[4] <= b[4]:
        b[4] -= a[4]
        a[4] = 0
    else:
        a[4] -= b[4]
        b[4] = 0
        if a[4] > b[5]:
            print("No")
            return
        b[5] -= a[4]
        b[1] += a[4]
        a[4] = 0

    b[3] += b[5]
    b[2] += b[5]
    b[5] = 0
    if a[3] <= b[3]:
        b[3] -= a[3]
        a[3] = 0
    else:
        a[3] -= b[3]
        b[3] = 0
        if a[3] > b[4]:
            print("No")
            return
        b[4] -= a[3]
        b[1] += a[3]
        a[3] = 0
    b[2] += b[4] * 2
    b[4] = 0

    if a[2] <= b[2]:
        b[2] -= a[2]
        a[2] = 0
    else:
        a[2] -= b[2]
        b[2] = 0
        if a[2] > b[3]:
            print("No")
            return
        b[3] -= a[2]
        b[1] += a[2]
        a[2] = 0
    b[1] += b[3] * 3
    b[3] = 0
    b[1] += b[2] * 2
    b[2] = 0
    if a[1] <= b[1]:
        print("Yes")
    else:
        print("No")


def main() -> None:
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()

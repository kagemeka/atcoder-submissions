import math


def main() -> None:
    # precompute commulative GCD from both left and right.

    n = int(input())
    a = list(map(int, input().split()))
    gcd_left = [0] * (n + 1)
    gcd_right = [0] * (n + 1)
    for i in range(n):
        gcd_left[i + 1] = math.gcd(gcd_left[i], a[i])
    for i in range(n - 1, -1, -1):
        gcd_right[i] = math.gcd(gcd_right[i + 1], a[i])

    mx = 0
    for i in range(n):
        mx = max(mx, math.gcd(gcd_left[i], gcd_right[i + 1]))
    print(mx)


if __name__ == "__main__":
    main()

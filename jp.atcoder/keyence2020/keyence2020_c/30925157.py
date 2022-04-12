import math


def main() -> None:
    n, k, s = map(int, input().split())

    if k == 0:
        a = [s + 1] * n
    else:
        a = [0] * n
        a[0] = s
        for i in range(k, n):
            a[i] = s + 1
    print(*a)


if __name__ == "__main__":
    main()

import math


def main() -> None:
    n, k, s = map(int, input().split())

    mx = 10**9
    a = [s] * n
    for i in range(k, n):
        a[i] = (s + 1) % mx
    print(*a)


if __name__ == "__main__":
    main()

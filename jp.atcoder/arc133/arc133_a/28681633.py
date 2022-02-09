import typing


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    x = -1
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            x = a[i]
            break
    if x == -1:
        x = a[-1]
    a = [y for y in a if y != x]
    print(*a)


if __name__ == "__main__":
    main()

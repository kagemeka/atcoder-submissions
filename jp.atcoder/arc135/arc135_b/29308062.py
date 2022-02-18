import typing


def main() -> None:
    n = int(input())
    s = list(map(int, input().split()))

    a = [-1] * (n + 2)
    a[0] = a[1] = a[2] = 0
    for i in range(n - 1):
        a[i + 3] = a[i] + s[i + 1] - s[i]
    for j in range(3):
        mn = min(a[i] for i in range(j, n + 2, 3))
        for i in range(j, n + 2, 3):
            a[i] -= mn

    delta = s[0] - sum(a[:3])
    if delta < 0:
        print("No")
        return
    for i in range(0, n + 2, 3):
        a[i] += delta

    for i in range(n):
        if a[i] + a[i + 1] + a[i + 2] != s[i]:
            print("No")
            return
    print('Yes')
    print(*a)


if __name__ == "__main__":
    main()

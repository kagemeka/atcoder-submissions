import typing


def main() -> None:
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()

    j = 0
    res = [False] * n
    for i in range(n):
        if s[i] == t[j]:
            res[i] = True
            j += 1
    for i in range(n):
        print("Yes" if res[i] else "No")


if __name__ == "__main__":
    main()

import typing


def solve(a: int, s: int) -> None:
    d = s - 2 * a
    if d < 0:
        print("No")
        return
    for i in range(60):
        if d >> i & 1 and a >> i & 1:
            print("No")
            return
    print("Yes")


def main() -> None:
    t = int(input())
    query = [tuple(map(int, input().split())) for _ in range(t)]
    for a, s in query:
        solve(a, s)


if __name__ == "__main__":
    main()

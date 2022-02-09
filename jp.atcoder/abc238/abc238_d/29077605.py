import typing


def solve(a: int, s: int) -> None:
    print("Yes" if (s - 2 * a) >= 0 else "No")


def main() -> None:
    t = int(input())
    for _ in range(t):
        a, s = map(int, input().split())
        solve(a, s)


if __name__ == "__main__":
    main()

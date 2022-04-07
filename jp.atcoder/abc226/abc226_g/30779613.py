def solve() -> None:
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))

    def pack(i: int, j: int) -> None:
        c = min(a[i], b[j])
        a[i] -= c
        b[j] -= c
        b[j - i] += c

    pack(5, 5)
    pack(4, 4)
    pack(4, 5)
    pack(3, 3)
    pack(3, 5)
    pack(3, 4)
    for i in range(4):
        pack(2, 5 - i)
    for i in range(5):
        pack(1, 5 - i)

    print("Yes" if sum(a[1:]) == 0 else "No")


def main() -> None:
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()

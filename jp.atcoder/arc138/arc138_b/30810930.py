def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    now = 0
    l = 0
    r = n - 1
    for _ in range(n):
        if a[r] == now:
            r -= 1
            continue
        if a[l] != now:
            print("No")
            return
        l += 1
        now ^= 1
    assert r == l - 1
    print("Yes")


if __name__ == "__main__":
    main()

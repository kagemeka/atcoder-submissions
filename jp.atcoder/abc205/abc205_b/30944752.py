def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        if a[i] == i + 1:
            continue
        print("No")
        return
    print("Yes")


if __name__ == "__main__":
    main()

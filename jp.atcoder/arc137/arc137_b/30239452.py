def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    max_diff = 0
    min_diff = 0
    mx = 0
    mn = 0
    s = 0
    for x in a:
        if x == 1:
            s += 1
        else:
            s -= 1
        max_diff = max(max_diff, s - mn)
        min_diff = min(min_diff, s - mx)
        mx = max(mx, s)
        mn = min(mn, s)
    print(max_diff - min_diff + 1)


if __name__ == "__main__":
    main()

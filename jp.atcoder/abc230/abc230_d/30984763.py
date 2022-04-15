def main() -> None:
    n, d = map(int, input().split())
    lr = [tuple(map(int, input().split())) for _ in range(n)]
    lr.sort(key=lambda x: x[1])

    count = 0
    last = 0
    for l, r in lr:
        if l <= last:
            continue
        last = r + d - 1
        count += 1
    print(count)


if __name__ == "__main__":
    main()

def main() -> None:
    n = int(input())
    t, average = map(int, input().split())
    t *= 1000
    average *= 1000
    h = list(map(int, input().split()))
    temperature = [t - x * 6 for x in h]

    index = -1
    min_diff = 1 << 30
    for i in range(n):
        diff = abs(temperature[i] - average)
        if diff >= min_diff:
            continue
        min_diff = diff
        index = i
    print(index + 1)


if __name__ == "__main__":
    main()

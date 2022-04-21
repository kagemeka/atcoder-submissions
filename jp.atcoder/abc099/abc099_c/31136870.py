def main() -> None:

    preset_1_time = set()
    for i in range(10):
        preset_1_time.add(pow(6, i))
        preset_1_time.add(pow(9, i))
    INF = 1 << 60

    K = 1 << 17
    min_count = [INF] * K
    min_count[0] = 0
    for x in preset_1_time:
        if x < K:
            min_count[x] = 1

    for i in range(K):
        if min_count[i] != INF:
            continue
        for x in preset_1_time:
            j = i - x
            if j < 0:
                continue
            min_count[i] = min(min_count[i], min_count[j] + 1)

    print(min_count[int(input())])


if __name__ == "__main__":
    main()

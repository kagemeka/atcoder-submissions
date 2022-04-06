def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    K = 1 << 20
    divisor_count = [0] * K
    for x in a:
        divisor_count[x] += 1

    for x in range(K - 1, 0, -1):
        if divisor_count[x] == 0:
            continue
        for i in range(x * 2, K, x):
            divisor_count[i] += divisor_count[x]

    count = sum(divisor_count[x] == 1 for x in a)
    print(count)


if __name__ == "__main__":
    main()

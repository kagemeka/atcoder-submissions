def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    K = 1 << 20
    divisor_count = [0] * K
    for x in a:
        divisor_count[x] += 1

    for i in range(K - 1, 0, -1):
        for j in range(i * 2, K, i):
            divisor_count[j] += divisor_count[i]

    count = sum(divisor_count[x] == 1 for x in a)
    print(count)


if __name__ == "__main__":
    main()

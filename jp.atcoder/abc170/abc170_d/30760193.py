def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    K = 1 << 20
    divisor_count = [0] * K

    a.sort()
    for x in a:
        for i in range(x, K, x):
            divisor_count[i] += 1

    count = sum(divisor_count[x] == 1 for x in a)
    print(count)


if __name__ == "__main__":
    main()

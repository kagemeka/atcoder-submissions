def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    K = 1 << 18
    count = [0] * K
    for x in a:
        count[x] += 1

    tot = 0
    for j in range(1, K):
        for i in range(j, K, j):
            tot += count[i] * count[j] * count[i // j]
    print(tot)


if __name__ == "__main__":
    main()

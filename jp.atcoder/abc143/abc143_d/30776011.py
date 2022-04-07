def main() -> None:
    n = int(input())
    length = list(map(int, input().split()))

    length.sort()

    count = 0
    for i in range(n - 2):
        r = i + 2
        for j in range(i + 1, n - 1):

            while r < n and length[r] < length[i] + length[j]:
                r += 1
            count += r - j - 1
    print(count)


if __name__ == "__main__":
    main()

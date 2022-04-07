def main() -> None:
    n = int(input())
    length = list(map(int, input().split()))
    length.sort()
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if length[j] == length[i]:
                continue
            for k in range(j + 1, n):
                if length[k] == length[j]:
                    continue
                if length[k] >= length[i] + length[j]:
                    break
                count += 1
    print(count)


if __name__ == "__main__":
    main()

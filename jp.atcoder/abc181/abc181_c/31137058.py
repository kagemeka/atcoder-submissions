def main() -> None:
    n = int(input())
    x, y = [], []
    for _ in range(n):
        i, j = map(int, input().split())
        x.append(i)
        y.append(j)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (y[j] - y[i]) * (x[k] - x[j]) == (y[k] - y[j]) * (x[j] - x[i]):
                    print("Yes")
                    return
    print("No")


if __name__ == "__main__":
    main()

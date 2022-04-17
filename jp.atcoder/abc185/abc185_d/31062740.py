def main() -> None:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(0)
    a.append(n + 1)
    a.sort()

    diffs = [a[i + 1] - a[i] - 1 for i in range(m + 1) if a[i + 1] - a[i] > 1]
    if not diffs:
        print(0)
        return
    k = min(diffs)
    print(sum((d + k - 1) // k for d in diffs))


if __name__ == "__main__":
    main()

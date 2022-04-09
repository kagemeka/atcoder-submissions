def main() -> None:
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    print(sum(h) - sum(h[:k]))


if __name__ == "__main__":
    main()

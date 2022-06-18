def main() -> None:
    import collections
    n = int(input())
    count = collections.Counter(input() for _ in range(n))
    order = sorted(count.items(), key=lambda x: x[1])
    print(order[-1][0])


if __name__ == "__main__":
    main()

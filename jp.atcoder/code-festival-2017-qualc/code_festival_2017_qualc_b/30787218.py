
def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    even_count = sum(a[i] & 1 == 0 for i in range(n))

    print(3**n - 2**even_count)


if __name__ == "__main__":
    main()

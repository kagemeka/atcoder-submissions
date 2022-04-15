def main() -> None:
    n = int(input())
    print(sum(len(str(i)) & 1 for i in range(1, n + 1)))


if __name__ == "__main__":
    main()

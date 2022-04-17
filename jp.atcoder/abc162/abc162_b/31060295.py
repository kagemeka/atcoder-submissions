def main() -> None:
    n = int(input())

    s = (1 + n) * n // 2
    s -= (3 + n // 3 * 3) * (n // 3) // 2
    s -= (5 + n // 5 * 5) * (n // 5) // 2
    s += (15 + n // 15 * 15) * (n // 15) // 2
    print(s)


if __name__ == "__main__":
    main()

def main() -> None:
    x = int(input())
    q, r = divmod(x, 11)
    print(q * 2 + (r > 0) + (r > 6))


if __name__ == "__main__":
    main()

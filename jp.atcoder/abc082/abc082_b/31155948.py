def main() -> None:
    print("Yes" if sorted(input()) < sorted(input(), reverse=1) else "No")


if __name__ == "__main__":
    main()

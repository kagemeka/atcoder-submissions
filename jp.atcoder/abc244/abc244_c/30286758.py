def main() -> None:
    n = int(input())
    s = set(range(1, 2 * n + 2))
    for i in range(n + 1):
        print(s.pop(), flush=True)
        x = int(input())
        if i != n:
            s.remove(x)
    # x = int(input())


if __name__ == "__main__":
    main()

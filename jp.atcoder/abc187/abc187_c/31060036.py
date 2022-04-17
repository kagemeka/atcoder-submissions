def main() -> None:
    n = int(input())
    strings = [input() for _ in range(n)]

    a = set()
    b = set()
    for s in strings:
        if s[0] == "!":
            a.add(s[1:])
        else:
            b.add(s)

    c = a & b
    print("satisfiable" if not c else c.pop())


if __name__ == "__main__":
    main()

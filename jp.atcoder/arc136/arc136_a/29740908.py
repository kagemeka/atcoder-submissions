def main() -> None:
    n = int(input())
    s = list(input())

    for i in range(n - 1):
        if s[i] == "B" and s[i + 1] == "A":
            s[i] = "A"
            s[i + 1] = "B"
        elif s[i] == s[i + 1] == "B":
            s[i] = ""
            s[i + 1] = "A"
    print("".join(s))


main()

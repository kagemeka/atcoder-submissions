def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    appeared = [False] * 2001
    for x in a:
        appeared[x] = True

    for i in range(2001):
        if appeared[i]:
            continue
        print(i)
        return


if __name__ == "__main__":
    main()

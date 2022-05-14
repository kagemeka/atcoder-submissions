def main() -> None:
    n = int(input())
    used = set()
    mx = 0
    index = -1
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s in used:
            continue
        used.add(s)
        if t > mx:
            mx = t
            index = i
    print(index + 1)


if __name__ == "__main__":
    main()

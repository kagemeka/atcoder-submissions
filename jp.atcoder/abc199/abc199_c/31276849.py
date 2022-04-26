def main() -> None:
    n = int(input())
    s = list(input())
    q = int(input())

    length = 2 * n
    swapped = 0

    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 2:
            swapped ^= 1
            continue
        a -= 1
        b -= 1
        a = (a + swapped * n) % length
        b = (b + swapped * n) % length
        s[a], s[b] = s[b], s[a]
    if swapped:
        s = s[n:] + s[:n]
    print("".join(s))


if __name__ == "__main__":
    main()

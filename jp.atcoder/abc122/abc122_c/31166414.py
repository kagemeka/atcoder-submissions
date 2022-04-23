def main() -> None:
    n, q = map(int, input().split())
    s = input()

    count = [0] * n
    for i in range(1, n):
        count[i] = count[i - 1] + (s[i - 1 : i + 1] == "AC")
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        print(count[r] - count[l])


if __name__ == "__main__":
    main()

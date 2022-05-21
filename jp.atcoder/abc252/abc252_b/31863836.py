def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    mx = max(a)
    cand = [i + 1 for i in range(n) if a[i] == mx]
    b = list(map(int, input().split()))
    print("Yes" if set(cand) & set(b) else "No")


if __name__ == "__main__":
    main()

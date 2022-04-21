def main() -> None:
    n = int(input())
    t = [0, 0, 1]
    K = 1 << 20
    MOD = 10**4 + 7
    for _ in range(K):
        t.append((t[-3] + t[-2] + t[-1]) % MOD)
    print(t[n - 1])


if __name__ == "__main__":
    main()

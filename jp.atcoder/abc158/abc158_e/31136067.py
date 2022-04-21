def main() -> None:
    # if [l, r] is multiple of p,
    # rem[r] = rem[l - 1] * 10^(r - l + 1)  mod p
    # fix l and count up r
    n, p = map(int, input().split())
    a = list(map(int, input()))

    rem = [0] * (n + 1)
    for i in range(n):
        rem[i + 1] = (rem[i] * 10 + a[i]) % p

    pow_10 = [1] * (n + 1)
    for i in range(n):
        pow_10[i + 1] = pow_10[i] * 10 % p

    # instead of compute 10^(r - l + 1) for each r when fixing l (relative),
    # count add to rem[r] * 10 ^ (n - r) in advance.
    # and check count[rem[l] * 10 ^ (n - l)] (absolute)
    count = [0] * p
    tot = 0
    for i in range(n, -1, -1):
        j = rem[i] * pow_10[n - i] % p
        tot += count[j]
        count[j] += 1

    print(tot)


if __name__ == "__main__":
    main()

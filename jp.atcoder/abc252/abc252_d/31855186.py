import collections


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    b = list(collections.Counter(a).values())

    mx = max(b)
    cc = [0] * (mx + 1)
    for c in b:
        cc[c] += 1

    def choose_3(n):
        return n * (n - 1) * (n - 2) // 6

    def choose_2(n):
        return n * (n - 1) // 2

    tot = 0
    for i in range(mx + 1):
        tot += choose_3(cc[i]) * i**3
        tot += choose_2(cc[i]) * i**2 * (n - cc[i] * i)

    s = [cc[i] * i for i in range(mx + 1)]
    for i in range(mx):
        s[i + 1] += s[i]

    for i in range(mx):
        for j in range(i + 1, mx + 1):
            if cc[i] == 0 or cc[j] == 0:
                continue
            tot += cc[i] * i * cc[j] * j * (n - s[j])
    print(tot)


if __name__ == "__main__":
    main()

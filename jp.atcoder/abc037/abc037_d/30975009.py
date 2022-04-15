import sys


def main() -> None:
    h, w = map(int, sys.stdin.readline().split())

    n = h * w
    g = [[] for _ in range(n)]
    a = [0] * n
    for i in range(h):
        row = list(map(int, sys.stdin.readline().split()))
        for j in range(w):
            a[i * w + j] = row[j]

    for i in range(n - w):
        if a[i] < a[i + w]:
            g[i].append(i + w)
        elif a[i] > a[i + w]:
            g[i + w].append(i)

    for i in range(n - 1):
        if i % w == w - 1:
            continue
        if a[i] < a[i + 1]:
            g[i].append(i + 1)
        elif a[i] > a[i + 1]:
            g[i + 1].append(i)

    MOD = 10**9 + 7
    count = [1] * n
    for i in sorted(range(n), key=lambda i: a[i]):
        count[i] %= MOD
        for j in g[i]:
            count[j] += count[i]

    print(sum(count) % MOD)


if __name__ == "__main__":
    main()

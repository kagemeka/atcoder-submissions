import collections


def main() -> None:
    # sum of odd potisions is same to sum of even positions
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = a[i] if i & 1 else -a[i]

    for i in range(n):
        s[i + 1] += s[i]

    count = collections.defaultdict(int)
    tot = 0
    for i in range(n + 1):
        tot += count[s[i]]
        count[s[i]] += 1
    print(tot)


if __name__ == "__main__":
    main()

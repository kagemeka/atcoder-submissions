import collections


def main() -> None:
    n, k = map(int, input().split())
    color = list(map(int, input().split()))
    count_color = collections.Counter()
    count_kind = 0

    for i in range(k):
        c = color[i]
        if count_color[c] == 0:
            count_kind += 1
        count_color[c] += 1

    mx = count_kind
    for i in range(k, n):
        c = color[i - k]
        count_color[c] -= 1
        if count_color[c] == 0:
            count_kind -= 1
        c = color[i]
        if count_color[c] == 0:
            count_kind += 1
        count_color[c] += 1
        mx = max(mx, count_kind)
    print(mx)


if __name__ == "__main__":
    main()

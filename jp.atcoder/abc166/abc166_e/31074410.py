import collections


def main() -> None:
    n = int(input())
    # j > i, j - i = a_i + a_j
    # j - a_j = a_i + i
    # b_i = a_i + i
    # c_i = i - a_i
    # count pairs b_i == c_j
    a = list(map(int, input().split()))
    b = [a[i] + i + 1 for i in range(n)]
    c = [i + 1 - a[i] for i in range(n)]
    # b_i != c_i (a_i >= 1)

    cb = collections.Counter(b)
    cc = collections.Counter(c)

    print(sum(cc[i] * v for i, v in cb.items()))


if __name__ == "__main__":
    main()

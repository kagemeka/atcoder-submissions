def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    # b = sorted(a)
    # border = b[n // 2]
    # bl = [x >= border for x in a]
    # print(bl)
    # print(sum(b[n // 2 :]))

    # replace each value with -1 or 1
    # if less than half border -> -1
    # other more than half border -> 1
    # left half cumsum should be less than or equal to 0
    # it's can be always satisfied.

    sorted_index = sorted(range(n), key=lambda i: a[i])

    v = [0] * n
    for i in range(n):
        v[sorted_index[i]] = 1 if i >= n // 2 else -1

    s = sum(a[i] for i in range(n) if v[i] == 1)
    # print(v)

    # cumsum = [0] * (n + 1)
    # for i in range(n):
    #     cumsum[i + 1] = cumsum[i] + v[i]
    # print(cumsum)

    for i in range(n - 1):
        v[i + 1] += v[i]
    # search hill top

    # argmax
    argmax = 0
    for i in range(n):
        if v[i] > v[argmax]:
            argmax = i
    k = (argmax + 1) % n

    print(k, s)


if __name__ == "__main__":
    main()

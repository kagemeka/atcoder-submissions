def main() -> None:
    # fn_n(...f_1(x)) is monotonic increasing on x.
    # sort the x list at first.
    # max -> all the value left than a certain border become a_i
    # min -> all the value right than a certain border become a_i
    # add -> add a_i to each value.
    # memorize original query index and retriave at last.
    n = int(input())
    at = [tuple(map(int, input().split())) for _ in range(n)]
    q = int(input())
    queries = list(map(int, input().split()))
    sorted_index = sorted(range(q), key=lambda i: queries[i])

    x = [queries[i] for i in sorted_index]

    left, right = -1, q
    d = 0
    for a, t in at:
        if t == 1:
            d += a
        elif t == 2:
            while left < min(right, q - 1) and x[left + 1] + d <= a:
                left += 1
                x[left] = a - d
            if left == right:
                x[left] = max(x[left], a - d)
        else:
            while right > max(left, 0) and x[right - 1] + d >= a:
                right -= 1
                x[right] = a - d
            if right == left:
                x[right] = min(x[right], a - d)
    for i in range(left):
        x[i] = x[left]
    for i in range(right + 1, q):
        x[i] = x[right]
    for i in range(q):
        x[i] += d
    result = [0] * q
    for i in range(q):
        result[sorted_index[i]] = x[i]
    print(*result, sep="\n")


if __name__ == "__main__":
    main()

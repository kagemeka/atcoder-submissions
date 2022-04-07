def main() -> None:
    # only 4 patterns of weight.

    n, capacity = map(int, input().split())
    wv = [tuple(map(int, input().split())) for _ in range(n)]

    values = [[] for _ in range(4)]
    w0 = wv[0][0]

    for w, v in wv:
        values[w - w0].append(v)
    for i in range(4):
        values[i].sort(reverse=True)

    cumsum_values = [[0] * (len(values[i]) + 1) for i in range(4)]
    for i in range(4):
        for j in range(len(values[i])):
            cumsum_values[i][j + 1] = cumsum_values[i][j] + values[i][j]

    max_value = 0
    for i in range(len(cumsum_values[0])):
        for j in range(len(cumsum_values[1])):
            for k in range(len(cumsum_values[2])):
                for l in range(len(cumsum_values[3])):
                    weight = w0 * (i + j + k + l) + j + 2 * k + 3 * l
                    if weight > capacity:
                        continue

                    value = (
                        cumsum_values[0][i]
                        + cumsum_values[1][j]
                        + cumsum_values[2][k]
                        + cumsum_values[3][l]
                    )
                    max_value = max(max_value, value)
    print(max_value)


if __name__ == "__main__":
    main()

def main() -> None:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    x_indices = []
    y_indices = []
    for i in range(n):
        if a[i] == x:
            x_indices.append(i)
        if a[i] == y:
            y_indices.append(i)

    # shakutori method

    xi = yi = 0
    count = 0
    j = 0
    for i in range(n):
        if not y <= a[i] <= x:
            continue
        while xi < len(x_indices) and x_indices[xi] < i:
            xi += 1
        if xi == len(x_indices):
            break
        while yi < len(y_indices) and y_indices[yi] < i:
            yi += 1
        if yi == len(y_indices):
            break
        left = max(x_indices[xi], y_indices[yi])

        j = max(j, i)
        while j < n and y <= a[j] <= x:
            j += 1
        if j < left:
            continue
        count += j - left
        # print(i, left, j, count)
    print(count)


if __name__ == "__main__":
    main()

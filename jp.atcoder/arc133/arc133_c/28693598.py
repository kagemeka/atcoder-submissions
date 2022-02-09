import typing


def main() -> None:
    h, w, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    y = (k - 1) * (h - 1)
    x = (k - 1) * (w - 1)
    s = y * (w - 1)
    y %= k
    x %= k
    y_val = [0] * h
    x_val = [0] * w
    for i in range(1, h):
        y_val[i] = (a[i] - x) % k
    for j in range(1, w):
        x_val[j] = (b[j] - y) % k
    y_val[0] = (b[0] - sum(y_val)) % k
    x_val[0] = (a[0] - sum(x_val)) % k
    if y_val[0] != x_val[0]:
        print(-1)
        return
    s += sum(y_val) + sum(x_val) - y_val[0]
    # if cycle possible,
    # s += k
    i, j = 1, 1
    v = y_val[0]
    while i < h and j < w:
        if y_val[i] <= x_val[j]:
            d = k - 1 - x_val[j]
        d = k - 1 - max(y_val[i], x_val[j])
        x_val[j] += d
        y_val[i] += d
        if y_val[i] == k - 1:
            i += 1
        if x_val[j] == k - 1:
            j += 1
        v -= d
        if v < 0:
            s += k
            v %= k
    print(s)


if __name__ == "__main__":
    main()

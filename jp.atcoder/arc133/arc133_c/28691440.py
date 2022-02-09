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
    print(s)


if __name__ == "__main__":
    main()

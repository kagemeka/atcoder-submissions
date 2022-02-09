import typing


def main() -> typing.NoReturn:
    n, m = map(int, input().split())

    h = list(map(int, input().split()))
    w = list(map(int, input().split()))
    h.sort()
    w.sort()

    inf = 1 << 60
    mn = inf

    left_sum = [inf] * n
    for i in range(1, n, 2):
        left_sum[i] = h[i] - h[i - 1]
    for i in range(1, n - 2, 2):
        left_sum[i + 2] += left_sum[i]

    right_sum = [inf] * n
    for i in range(n - 2, -1, -2):
        right_sum[i] = h[i + 1] - h[i]
    for i in range(n - 2, 1, -2):
        right_sum[i - 2] += right_sum[i]
    j = 0
    for i in range(n):
        # pairing with i-th child.
        # teacher's height is w_j
        d = abs(w[j] - h[i])
        while w[j] < h[i] and j + 1 < n:
            j += 1
            d = min(d, abs(w[j] - h[i]))
        s = 0
        if i & 1:
            s += h[i + 1] - h[i - 1]
            if i - 2 >= 0:
                s += left_sum[i - 2]
            if i + 2 < n:
                s += right_sum[i + 2]
        else:
            if i - 1 >= 0:
                s += left_sum[i - 1]
            if i + 1 < n:
                s += right_sum[i + 1]
        mn = min(mn, s + d)
    print(mn)

main()

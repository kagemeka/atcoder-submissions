import typing


def main() -> None:
    n, q = map(int, input().split())

    # for each query,
    # 1. count up the black stones to reverse
    # 2. update some states.

    # - set range minimum, get point.
    # dual segment tree or lazy segment tree.
    # O(Q\log{N})

    # - memorize the minimum
    # in decending order of N for each x and y,
    # O(N + Q)

    min_y = [-1] * n
    min_x = [-1] * n

    mn_y = mn_x = n - 1
    y = x = n - 1
    cnt = (n - 2) * (n - 2)
    for _ in range(q):
        t, i = map(int, input().split())
        i -= 1
        if t == 1:
            while x > i:
                x -= 1
                min_y[x] = mn_y
            cnt -= min_y[i] - 1
            mn_x = min(mn_x, i)

        else:
            while y > i:
                y -= 1
                min_x[y] = mn_x
            cnt -= min_x[i] - 1
            mn_y = min(mn_y, i)

    print(cnt)

main()

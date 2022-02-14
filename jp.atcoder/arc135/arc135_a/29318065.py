import typing


def main() -> None:
    # a_i' = a_i ^ a_j
    # a_i'' = a_i' ^ a_j' = a_i ^ a_j ^ a_j ^ a_k = a_i ^ a_k
    # ...
    # Will be offset in the end.
    # thus, at most one time operation is needed.

    n = int(input())
    a = list(map(int, input().split()))
    M = 30
    bit_count = [0] * M
    for x in a:
        for i in range(M):
            bit_count[i] += x >> i & 1

    INF = 1 << 60
    mx = -INF
    for x in a:
        delta = 0
        for i in range(M):
            if ~x >> i & 1:
                continue
            delta += (n - 2 * bit_count[i]) * (1 << i)
        mx = max(delta, mx)

    s = sum(a)
    if mx >= 0:
        s += mx
    print(s)


if __name__ == "__main__":
    main()

import typing


def main() -> None:
    # DP

    n, q = map(int, input().split())
    known = [False] * (n + 1)
    known[0] = True
    lr = [tuple(map(int, input().split())) for _ in range(q)]
    lr.sort()
    for l, r in lr:
        known_l = known[r]
        known_r = known[l - 1]
        known[l - 1] |= known_l
        known[r] |= known_r
    print("Yes" if known[-1] else "No")


if __name__ == "__main__":
    main()

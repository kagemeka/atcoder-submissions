def main() -> None:
    # binary search minimum minutes

    # for each person, check left -> back -> right, or right -> back, left

    n, m = map(int, input().split())
    x = [int(input()) - 1 for _ in range(m)]

    # train [0, n)

    def possible(t: int) -> bool:
        done_index = -1
        for i in range(m):
            done_index = min(done_index, x[i] - 1)
            left_diff = x[i] - done_index - 1
            if left_diff > t:
                return False
            left_right = x[i] + (t - 2 * left_diff)
            right_left = x[i] + (t - left_diff) // 2
            done_index = max(left_right, right_left, x[i])

        return done_index >= n - 1

    def binary_search() -> int:
        lo, hi = -1, 1 << 30  # impossible, possible

        while hi - lo > 1:
            t = (lo + hi) >> 1
            if possible(t):
                hi = t
            else:
                lo = t
        return hi

    print(binary_search())


if __name__ == "__main__":
    main()

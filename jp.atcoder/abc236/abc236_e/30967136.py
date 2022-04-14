def main() -> None:
    # binary search
    n = int(input())
    a = list(map(int, input().split()))

    def binary_search_average() -> float:
        def possible_more_than(average: float) -> bool:
            b = [x - average for x in a]
            dp = [[0.0, 0.0] for _ in range(n + 1)]
            # not-choose, choose
            # max sum
            for i in range(n):
                dp[i + 1][0] = dp[i][1]
                dp[i + 1][1] = max(dp[i]) + b[i]
            return max(dp[-1]) >= 0

        lo, hi = 0, 1 << 30  # possible, impossible
        for _ in range(50):
            average = (lo + hi) / 2
            if possible_more_than(average):
                lo = average
            else:
                hi = average

        return lo

    def binary_search_median() -> int:
        def possible_more_than(median: int) -> bool:
            v = 0
            count = 0
            prev_chosen = True
            for i in range(n):
                if a[i] >= median:
                    v += 1
                    count += 1
                    prev_chosen = True
                    continue
                if i == 0 or prev_chosen:
                    prev_chosen = False
                    continue
                v -= 1
                count += 1
                prev_chosen = True
            return v >= 1 if count & 1 else v >= 2

        lo, hi = 0, 1 << 30
        while hi - lo > 1:
            median = (lo + hi) // 2
            if possible_more_than(median):
                lo = median
            else:
                hi = median
        assert lo in a
        return lo

    print(binary_search_average())
    print(binary_search_median())


if __name__ == "__main__":
    main()

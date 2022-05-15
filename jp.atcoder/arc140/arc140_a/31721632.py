import string
import typing
import collections


def main() -> None:
    n, k = map(int, input().split())
    # brute force and greedy
    s = list(ord(x) - ord("a") for x in input())

    # check possibility

    def possible(i: int) -> bool:
        if n % i:
            return False
        r = k
        for j in range(i):
            count = [0] * 26

            r -= n // i - max(collections.Counter(s[j:n:i]).values())
        return r >= 0

    for i in range(1, n + 1):
        if not possible(i):
            continue
        print(i)
        return


if __name__ == "__main__":
    main()

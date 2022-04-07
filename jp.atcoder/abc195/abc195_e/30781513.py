import functools
import sys

sys.setrecursionlimit(1 << 20)


def main() -> None:
    n = int(input())
    s = list(map(lambda x: int(x) % 7, input()))
    x = input()

    nxt = [i * 10 % 7 for i in range(7)]
    prev = [-1] * 7
    for i in range(7):
        prev[nxt[i]] = i
    print(nxt)

    @functools.lru_cache(maxsize=None)
    def gonnabe(i: int, rem: int) -> bool:
        if x[i] == "T":
            if i == n - 1:
                return (rem + s[i]) % 7 == 0 or rem == 0
            return gonnabe(i + 1, (rem + s[i]) * 10 % 7) or gonnabe(
                i + 1,
                rem * 10 % 7,
            )
        else:
            if i == n - 1:
                return s[i] == rem == 0
            return gonnabe(i + 1, (rem + s[i]) * 10 % 7) and gonnabe(
                i + 1,
                rem * 10 % 7,
            )

    if gonnabe(0, 0):
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()

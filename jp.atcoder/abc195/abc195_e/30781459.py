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

    @functools.lru_cache(maxsize=None)
    def gonnabe(i: int, rem: int) -> bool:
        if x[i] == "T":
            if i == 0:
                return s[i] == rem or rem == 0
            return gonnabe(i - 1, prev[rem]) or gonnabe(
                i - 1,
                prev[(rem - s[i]) % 7],
            )
        else:
            if i == 0:
                return s[i] == rem and rem == 0
            return gonnabe(i - 1, prev[rem]) and gonnabe(
                i - 1,
                prev[(rem - s[i]) % 7],
            )

    if gonnabe(n - 1, 0):
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()

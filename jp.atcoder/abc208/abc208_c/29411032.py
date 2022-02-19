from __future__ import annotations


def argsort(arr: list[int]) -> list[int]:
    return sorted(range(len(arr)), key=lambda i: arr[i])


def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # argsort
    # array compression + argsort permutation
    a = argsort(a)
    q, r = divmod(k, n)
    count = [q] * n
    for i in a[:r]:
        count[i] += 1
    print(*count, sep="\n")


main()

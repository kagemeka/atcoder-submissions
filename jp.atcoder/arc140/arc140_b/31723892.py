import string
import typing
import collections


def main() -> None:
    # count '...AARCC...'
    n = int(input())
    s = input()
    counts = []
    for i in range(n):
        if s[i] != "R":
            continue
        j = 0
        while True:
            j += 1
            if j < 0 or j >= n:
                break
            if not (s[i - j] == "A" and s[i + j] == "C"):
                break
        j -= 1
        if j == 0:
            continue
        counts.append(j)
    counts.sort(reverse=True)
    l = 0
    for i in range(n):
        if l >= len(counts):
            break
        if i & 1 == 0:
            counts[l] -= 1
            if counts[l] == 0:
                l += 1
        else:
            counts.pop()
    print(i)


if __name__ == "__main__":
    main()

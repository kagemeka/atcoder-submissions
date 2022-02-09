import typing
import itertools
import bisect
import operator
import functools


def verbal_arithemetic(
    words: list[str],
    result: str,
    zero_ok: bool=True,
) -> list[dict[str, int]]:
    r"""Solve verbal arthmetic."""
    words = words.copy()
    words.append(result)
    letters = sorted(functools.reduce(operator.or_, map(set, words), set()))
    words = [[bisect.bisect_left(letters, l) for l in w] for w in words]
    n, m = len(words), max(map(len, words))
    value = [-1] * 10
    digit = [-1] * len(letters)
    patterns = []

    def search(i: int, j: int, s: int): # type annotation
        if j >= m:
            if s == 0: patterns.append(dict(zip(letters, digit)))
            return
        if i == n:
            if s % 10 == 0: search(0, j + 1, s // 10)
            return
        w = words[i]
        if j >= len(w): search(i + 1, j, s); return
        sign = (i < n - 1) * 2 - 1
        v = w[~j]
        def no_heading_zero(d: int) -> bool:
            return d != 0 or j < len(w) - 1 or zero_ok and j == 0
        if digit[v] != -1:
            if not no_heading_zero(digit[v]): return
            search(i + 1, j, s + sign * digit[v])
            return
        for d in range(10):
            if value[d] != -1: continue
            if not no_heading_zero(d): continue
            digit[v], value[d] = d, v
            search(i + 1, j, s + sign * d)
            digit[v] = value[d] = -1

    search(0, 0, 0)
    return patterns


import sys

def main() -> typing.NoReturn:
    s = sys.stdin.read().split()
    words, result = s[:-1], s[-1]
    patterns = verbal_arithemetic(words, result, zero_ok=False)

    if not patterns:
        print('UNSOLVABLE')
        return
    p = patterns[0]

    def convert(l: str) -> str: return str(p[l])

    s = [''.join(map(convert, w)) for w in s]
    print(*s, sep='\n')


main()

import sys
from functools import reduce
from operator import mul
import math

def nCr(n, r):
    r = min(r, n-r)
    upper = reduce(mul, range(n, n-r, -1), 1)
    lower = reduce(mul, range(r, 0, -1), 1)
    return upper // lower


def oddCaseK(n, k):
    cand = 0
    for x in range(1, n+1):
        if x % k == 0:
            cand += 1

    number_of_possibles = 0
    if cand >= 1:
        number_of_possibles += cand
    if cand >= 2:
        number_of_possibles += nCr(cand, 2) * nCr(2, 1) * 3
    if cand >= 3:
        number_of_possibles += nCr(cand, 3) * math.factorial(3)

    return number_of_possibles



def evenCaseK(n, k):
    cand1 = 0
    cand2 = 0
    for x in range(1, n+1):
        if x % k == 0:
            cand1 += 1
        elif x % k == k // 2:
            cand2 += 1

    number_of_possibles = 0
    for cand in [cand1, cand2]:
        if cand >= 1:
            number_of_possibles += cand
        if cand >= 2:
            number_of_possibles += nCr(cand, 2) * nCr(2, 1) * 3
        if cand >= 3:
            number_of_possibles += nCr(cand, 3) * math.factorial(3)

    return number_of_possibles


def main():
    n, k = [int(x) for x in sys.stdin.readline().split()]
    if k % 2 == 0:
        ans = evenCaseK(n, k)
    else:
        ans = oddCaseK(n, k)

    print(ans)



if __name__ == "__main__":
    main()

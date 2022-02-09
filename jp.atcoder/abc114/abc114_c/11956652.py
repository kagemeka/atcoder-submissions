import sys
from itertools import product
from bisect import bisect_right as bi_r

cand = [int(''.join(p)) for i in range(3, 10)
        for p in product('357', repeat=i)
        if len(set(p)) == 3]

n = int(sys.stdin.readline().rstrip())

def main():
    print(bi_r(cand, n))

if __name__ ==  '__main__':
    main()

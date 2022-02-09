import sys
from collections import Counter
from itertools import combinations

n, *s = [s[0] for s in sys.stdin.read().split()]

def main():
    c = Counter(s)
    res = 0
    for i, j, k in combinations('MARCH', 3):
        res += c[i] * c[j] * c[k]
    print(res)

if __name__ ==  '__main__':
    main()

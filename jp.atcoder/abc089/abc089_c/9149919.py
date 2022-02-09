import sys
from collections import Counter
from itertools import combinations

MARCH = set('MARCH')

n = int(sys.stdin.readline().rstrip())
s = [x[0] for x in sys.stdin.read().split() if x[0] in MARCH]

def main():
    c = Counter(s)
    ways = 0
    for comb in combinations('MARCH', 3):
        res = 1
        for i in comb:
            res *= c.get(i, 0)
        ways += res

    return ways

if __name__ == '__main__':
    ans = main()
    print(ans)

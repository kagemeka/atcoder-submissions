import sys
from itertools import combinations

def main():
    n, s = sys.stdin.read().split()
    n = int(n)
    res = set()
    for comb in combinations(s, 3):
        res.add(comb)

    ans = len(res)
    print(ans)

if __name__ == '__main__':
    main()

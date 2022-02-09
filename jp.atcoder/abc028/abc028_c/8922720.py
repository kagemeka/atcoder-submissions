import sys
from itertools import combinations

*a, = map(int, sys.stdin.readline().split())

def main():
    res = set()
    for c in combinations(a, 3):
        res.add(sum(c))

    ans = sorted(res)[-3]
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

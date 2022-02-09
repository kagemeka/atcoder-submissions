import sys
from collections import Counter

n, *s = sys.stdin.read().split()
n = int(n)

def comb_2(n):
    return n * (n - 1) // 2

def main():
    t = [''.join(sorted(t)) for t in s]

    c = Counter(t)
    pairs_cnt = 0
    for v in c.values():
        pairs_cnt += comb_2(v)

    return pairs_cnt

if __name__ == '__main__':
    ans = main()
    print(ans)

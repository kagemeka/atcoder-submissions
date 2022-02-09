import sys
from collections import Counter

n, *s = sys.stdin.read().split()

def main():
    cnt = sorted(Counter(s).items(), key=lambda x: -x[1])
    m = cnt[0][1]
    ans = [s for s, c in cnt if c == m]
    print(*sorted(ans), sep='\n')


if __name__ ==  '__main__':
    main()

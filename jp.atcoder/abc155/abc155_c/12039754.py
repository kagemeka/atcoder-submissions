import sys
from collections import Counter

n, *s = sys.stdin.read().split()

def main():
    c = Counter(s)
    m = max(c.values())
    ans = [s for s, c in cnt.items() if c == m]
    print(*sorted(ans), sep='\n')

if __name__ ==  '__main__':
    main()

import sys
from collections import Counter

s = sys.stdin.readline().rstrip()

def main():
    c = Counter(s)
    res = c.get('+', 0) - c.get('-', 0)
    print(res)

if __name__ ==  '__main__':
    main()

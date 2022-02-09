import sys
from collections import Counter

s = sys.stdin.readline().rstrip()

def main():
    c = Counter(s)
    print(c.get('1', 0))

if __name__ ==  '__main__':
    main()

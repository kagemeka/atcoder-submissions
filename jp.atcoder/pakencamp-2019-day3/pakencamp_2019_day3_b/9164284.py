import sys
from collections import Counter

n, *s = sys.stdin.read().split()

def main():
    c = Counter(s)
    return 'black' if c.get('black', 0) > c.get('white', 0) else 'white'

if __name__ == '__main__':
    ans = main()
    print(ans)

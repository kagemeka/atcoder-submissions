import sys
from collections import Counter, OrderedDict

s = sys.stdin.readline().rstrip()

def main():
    c = Counter(s)
    for char in 'ABCDEF':
        yield c.get(char, 0)

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')

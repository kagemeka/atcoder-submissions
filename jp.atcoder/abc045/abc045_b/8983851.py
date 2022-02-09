import sys
from collections import deque

a, b, c = sys.stdin.read().split()

def main():
    deck = dict([('a', deque(a)), ('b', deque(b)), ('c', deque(c))])

    p = 'a'
    while True:
        if deck[p]:
            p = deck[p].popleft()
        else:
            return p.upper()

if __name__ == '__main__':
    ans = main()
    print(ans)

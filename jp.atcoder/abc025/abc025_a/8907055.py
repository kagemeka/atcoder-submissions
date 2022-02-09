import sys
from itertools import product

s, n = sys.stdin.read().split()
n = int(n)

def main():
    cand = list(map(lambda chars: ''.join(chars), product(s, repeat=2)))
    return cand[n-1]

if __name__ == '__main__':
    ans = main()
    print(ans)

import sys
from collections import Counter
from string import ascii_lowercase

INF = 50

n = int(sys.stdin.readline().rstrip())
strings = sys.stdin.read().split()

def main():
    shared = set(ascii_lowercase)
    for s in strings:
        shared &= set(s)

    cnts = [Counter(s) for s in strings]

    res = dict([(char, INF) for char in shared])

    for char in shared:
        for c in cnts:
            res[char] = min(res[char], c[char])

    ans = ''
    for char, c in sorted(res.items()):
        ans += char * c

    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

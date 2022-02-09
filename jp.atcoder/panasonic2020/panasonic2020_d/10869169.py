import sys
from string import ascii_lowercase

alphs = list(ascii_lowercase)

n = int(sys.stdin.readline().rstrip())

def main():
    cur = ['a']
    for _ in range(n-1):
        nex = []
        for s in cur:
            i = 0
            for c in s:
                i = max(i, ord(c) - 97)
            for al in alphs[:i+2]:
                nex.append(s + al)
        cur = nex
    return sorted(cur)

if __name__ == "__main__":
    ans = main()
    print(*ans, sep='\n')

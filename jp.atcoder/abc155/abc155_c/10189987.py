import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.read().split()

def main():
    c = Counter(s)
    ma = max(c.values())
    res = []
    for l, v in c.items():
        if v == ma:
            res.append(l)
    return sorted(res)

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')

import sys
from collections import Counter

s, t = sys.stdin.read().split()
t = int(t)

def main():
    c = Counter(s)
    u = c.get('U', 0)
    d = c.get('D', 0)
    l = c.get('L', 0)
    r = c.get('R', 0)
    cnt = c.get('?', 0)

    res = abs(u - d) + abs(l - r)
    if t == 1:
        ans = res + cnt
    else:
        if res >= cnt:
            ans = res - cnt
        else:
            ans = (cnt - res) % 2

    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)

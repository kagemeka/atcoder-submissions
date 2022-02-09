import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

def main():
    c = Counter(s)
    l = set()
    r = set(s)
    res = 0
    cnt = 0
    for letter in s:
        c[letter] -= 1
        if not c[letter]:
            r -= set([letter])
            if letter in l:
                cnt -= 1
        elif not letter in l:
            l.add(letter)
            cnt += 1
            res = max(res, cnt)
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
S = sys.stdin.read().split()

def main():
    for i in range(n):
        s = S[i]
        t = ''
        for c in s:
            if not t:
                t += c
            else:
                if t[-1] == '(' and c == ')':
                    t = t[:-1]
                else:
                    t += c
        S[i] = t

    res = deque(S[0])
    for s in S[1:]:
        if not s: continue
        l = len(s)
        if s[0] == ')':
            for i in range(l):
                if res and res[-1] == '(' and s[i] == ')':
                    res.pop()
                else:
                    for j in range(i, l):
                        res.append(s[j])
                    break
        else:
            for i in range(l-1, -1, -1):
                if res and res[0] == ')' and s[-1] == '(':
                    res.popleft()
                else:
                    for j in range(i, -1, -1):
                        res.appendleft(s[j])
                    break
    print('Yes' if not res else 'No')

if __name__ == '__main__':
    main()

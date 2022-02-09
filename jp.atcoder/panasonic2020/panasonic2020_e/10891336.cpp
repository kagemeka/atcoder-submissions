import sys
from itertools import permutations

a, b, c = sys.stdin.read().split()

def merge(s, t):
    n = len(s)
    m = len(t)
    cand = []
    for i in range(n):
        for j in range(min(m, n-i)):
            if s[i+j] != t[j]:
                if s[i+j] != '?' and t[j] != '?':
                    break
        else:
            if m >= n - i:
                cand.append(s[:i] + t)
            else:
                cand.append(s)
                break
    return cand

def main():
    ans = 10000
    for p in permutations((a, b, c)):
        s, t, u = p
        cand = merge(s, t)
        for w in cand:
            res = merge(w, u)
            for r in res:
                ans = min(ans, len(r))
    return ans

if __name__ == "__main__":
    ans = main()
    print(ans)

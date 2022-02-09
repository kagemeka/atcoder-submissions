import sys

n, *a = map(int, sys.stdin.read().split())
a = [0] + a

s = a.copy()
for i in range(n):
    s[i+1] += s[i]
se = [None] * (n + 1); se[0] = 0
for i in range(0, n - 1, 2):
    se[i+2] = a[i+2] + se[i]
for i in range(1, n + 1, 2):
    se[i] = se[i-1]

def dfs(l, r, c):
    if c == 0: return 0
    if not ((r - l + 1) & 1):
        s1 = se[r] - se[l-1]
        s2 = s[r] - se[r] - (s[l-1] - se[l-1])
        return max(s1, s2)
    if c == (r - l + 2) // 2:
        return sum(a[l:r+1:2])
    return max(a[l] + dfs(l + 2, r, c - 1), a[r] + dfs(l, r - 2, c - 1), dfs(l + 1, r - 1, c))

def main():
    print(dfs(1, n, n // 2))

if __name__ ==  '__main__':
    main()

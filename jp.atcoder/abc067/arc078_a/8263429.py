import sys
input = sys.stdin.readline

n = int(input())
a = [int(a) for a in input().split()]
s = [None] * n; s[0] = a[0]
for i in range(n-1): s[i+1] = s[i] + a[i+1]

mixi = abs(s[0] - (s[n-1] - s[0]))
for i in range(1, n-1): mixi = min(mixi, abs(s[i] - (s[n-1] - s[i])))   # 全部取るのはダメ

print(mixi)

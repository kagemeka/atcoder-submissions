from sys import stdin

n, a = (int(x) for x in stdin.read().split())
ans = n ** 2 - a
print(ans)

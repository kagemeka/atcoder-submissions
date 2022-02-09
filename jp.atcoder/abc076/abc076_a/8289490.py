import sys

r, g = (int(x) for x in sys.stdin.read().split())
ans = g * 2 - r
print(ans)

from sys import stdin

x, a, b = map(int, stdin.readline().split())
print('A' if abs(a - x) > abs(b - x) else "B")

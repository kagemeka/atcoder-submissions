import sys
x, t = (int(i) for i in sys.stdin.readline().split())
print(x - t if x > t else 0)

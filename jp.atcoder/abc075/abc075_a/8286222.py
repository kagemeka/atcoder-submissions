import sys

a, b, c = (int(x) for x in sys.stdin.readline().split())
if a == b:
    print(c)
elif b == c:
    print(a)
elif c == a:
    print(b)

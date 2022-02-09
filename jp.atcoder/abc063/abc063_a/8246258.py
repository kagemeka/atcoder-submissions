import sys
input = sys.stdin.readline

a, b = [int(x) for x in input().split()]

s = a + b

if s >= 10:
    print('error')
else:
    print(s)

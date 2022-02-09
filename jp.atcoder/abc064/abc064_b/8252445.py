import sys
input = sys.stdin.readline

N = int(input())
a = [int(a) for a in input().split()]
a.sort()
print(a[-1] - a[0])

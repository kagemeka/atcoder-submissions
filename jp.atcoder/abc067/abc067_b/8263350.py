import sys
input = sys.stdin.readline

n, k = [int(x) for x in input().split()]
l = [int(l) for l in input().split()]
l.sort(reverse=1)
print(sum(l[:k]))

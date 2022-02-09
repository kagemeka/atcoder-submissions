N = int(input())
T = [int(t) for t in input().split()]

M = int(input())
for i in range(M):
    t = T.copy()
    p, x = [int(x) for x in input().split()]
    t[p-1] = x
    print(sum(t))

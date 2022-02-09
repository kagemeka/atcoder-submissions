from sys import stdin
input = stdin.readline

N, K = [int(x) for x in input().split()]
arr = [0] * (10**5+1)
for _ in range(N):
    a, b = [int(x) for x in input().split()]
    arr[a] += b

remain = K
for i in range(1, 10**5+1):
    if arr[i] != 0:
        remain -= arr[i]
    if remain <= 0:
        print(i)
        exit()

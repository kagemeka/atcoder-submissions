N, K = [int(x) for x in input().split()]
arr = [0] * (10**5+1)
for _ in range(N):
    a, b = [int(x) for x in input().split()]
    arr[a] += b

th = 0
for i in range(1, 10**5+1):
    if arr[i] != 0:
        th += arr[i]
    if th >= K:
        print(i)
        exit()

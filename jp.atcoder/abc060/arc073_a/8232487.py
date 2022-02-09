N, T = [int(i) for i in input().split()]
t = [int(t) for t in input().split()]

total = T
for i in range(N-1):
    if t[i+1] - t[i] < T:
        total += t[i+1] - t[i]
    else:
        total += T
print(total)

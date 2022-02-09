n, k = [int(x) for x in input().split()]

arr = []
for i in range(n):
    a, b = [int(x) for x in input().split()]
    arr += [a] * b

arr.sort()

print(arr[k-1])

N, K = [int(x) for x in input().split()]
arr = {}
for _ in range(N):
    a, b = [int(x) for x in input().split()]
    if a in arr.keys():
        arr[a] += b
    else:
        arr.update({a: b})

s_a = {}# sorted arr
for key in sorted(arr.keys()):
    s_a.update({key: arr[key]})

th = 0
for i, c in s_a.items():
    th += c
    if th >= K:
        print(i)
        exit()

a, b, c = [int(x) for x in input().split()]

for i in range(1, b):
    if a * i % b == c:
        print("YES")
        break
else:
    print("NO")

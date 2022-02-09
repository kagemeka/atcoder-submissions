n, m = [int(x) for x in input().split()]
img_a = []
img_b = []

for i in range(n):
    img_a.append(input())

for i in range(m):
    img_b.append(input())

ans = "No"
for a in range(n - m + 1):
    for b in range(m):
        if img_b[b] in img_a[b+a]:
            if b == 0:
                index = img_a[a].index(img_b[0])
            current_index = img_a[b+a].index(img_b[b])

            if current_index != index:
                break
        else:
            break
    else:
        ans = "Yes"
        break

print(ans)

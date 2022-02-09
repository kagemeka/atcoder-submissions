n, m = [int(x) for x in input().split()]
img_a = []
img_b = []

for i in range(n):
    img_a.append(input())

for i in range(m):
    img_b.append(input())

ans = "No"
for a in range(n - m + 1):
    dup_a = img_a.copy()
    dup_b = img_b.copy()
    while True:
        for b in range(m):
            if dup_b[b] in dup_a[b+a]:
                if b == 0:
                    index = dup_a[a].index(dup_b[0])
                current_index = dup_a[b+a].index(dup_b[b])

                if current_index > index:
                    for line in dup_a:
                        del line[:current_index]
                        break
                elif current_index < index:
                    for line in dup_a:
                        del line[:index]
                        break

            else:   # if not substring in string.
                break
        else: # if not loop broken.
            ans = "Yes"
            break

print(ans)

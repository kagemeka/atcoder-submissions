n, m = [int(x) for x in input().split()]
img_a = []
img_b = []

for i in range(n):
    img_a.append(input())

for i in range(m):
    img_b.append(input())

ans = "No"
for a in range(n - m + 1):
    border = 0
    flag = True
    while flag:
        for b in range(m):
            if img_b[b] in img_a[b+a][border:]:
                if b == 0:
                    index = img_a[a].index(img_b[0], border)
                current_index = img_a[b+a].index(img_b[b], border)
                if current_index == index:
                    continue
                elif current_index > index:
                    border = current_index
                    break
                else:
                    border = index
                    break
            else:   # if not substring in string.
                flag = False
                break

        else: # if not loop broken.
            ans = "Yes"
            break


print(ans)

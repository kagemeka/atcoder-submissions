n, m = [int(x) for x in input().split()]
img_a = [input() for _ in range(n)]
img_b = [input() for _ in range(m)]

found = False
for a in range(n - m + 1):
    border = 0
    isok = True
    while isok and not found:
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
                isok = False
                break

        else: # if not loop broken.
            ans = "Yes"
            found = True
            break
    if found:
        break
else: # if not 'found==True' even after last loop, then it means B is not in A.
    ans = "No"

print(ans)

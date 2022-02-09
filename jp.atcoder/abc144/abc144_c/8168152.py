n = int(input())

for x in range(1, 10**6+1):
    if x**2 >= n:
        y = x
        break

i, j = y, y
for x in range(10**5):
    if i*j == n:
        ans = i + j - 2
        break
    elif i*j > n:
        i -= 1
    elif i*j < n:
        j += 1

print(ans)

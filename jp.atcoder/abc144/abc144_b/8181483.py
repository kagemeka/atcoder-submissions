n = int(input())

for i in range(1, 10):
    if n%i == 0:
        j = int(n / i)
        if j <= 9:
            ans = "Yes"
        else:
            ans = "No"
    else:
        ans = "No"
    if ans == "Yes":
        break

print(ans)

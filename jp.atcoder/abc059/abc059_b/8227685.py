a = input()
b = input()

ans = "EQUAL"
if len(a) > len(b):
    ans = "GREATER"
elif len(a) < len(b):
    ans = "LESS"
else:
    for i in range(len(a)):
        if a[i] != b[i]:
            if a[i] > b[i]:
                ans = 'GREATER'
                break
            else:
                ans = 'LESS'
                break

print(ans)

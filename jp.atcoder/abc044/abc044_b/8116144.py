w = input()
alphabets = set(w)
for alp in alphabets:
    if w.count(alp) % 2 != 0:
        ans = "No"
        break

else:
    ans = "Yes"

print(ans)

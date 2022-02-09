s = input()
letters = [letter for letter in s]

res = []

for letter in letters:
    if letter == "B":
        if res:
            res.pop()
    else:
        res.append(letter)

ans = ''.join(res)
print(ans)

o = input()
e = input()

lo = len(o)
le = len(e)
i = 0
res = []
while True:
    if i == len(o):
        break
    else:
        res.append(o[i])
    if i == len(e):
        break
    else:
        res.append(e[i])
        i += 1

print(''.join(res))

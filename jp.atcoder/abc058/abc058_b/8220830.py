o, e = input().split()

i = 0
res = []
while True:
    res.append(o[i])
    if e[i]:
        res.append(e[i])
        i += 1
    else:
        break

print(''.join(res))

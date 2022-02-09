o, e = input().split()

i = 0
res = []
while True:
    if o[i]:
        res.append(o[i])
    else:
        break
    if e[i]:
        res.append(e[i])
        i += 1
    else:
        break

print(''.join(res))

m = int(input())
if m < 100:
    vv = "00"
elif m >= 100 and m <= 5000:
    v = m * 10 / 1000
    if v < 10:
        vv = "0" + str(v)
    else:
        vv = str(v)
elif m >= 6000 and m <= 30000:
    vv = str(m //1000 + 50)
elif m >= 35000 and m <= 70000:
    vv = str((m // 1000 - 30) // 5 + 80)
elif m > 70000:
    vv = "89"

print(vv)

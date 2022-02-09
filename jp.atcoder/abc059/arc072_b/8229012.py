x, y = [int(i) for i in input().split()]

times = 0
while x >= 2 or y >= 2:
    if x >= y : # xから選ぶ
        if x % 2 == 0:
            y += x // 2
            x = 0
            times += 1
        else:
            y += (x - 1) // 2
            x = 1
            times += 1
    else:
        if y % 2 == 0:
            x += y // 2
            y = 0
            times += 1
        else:
            x += (y - 1) // 2
            y = 1
            times += 1

if times % 2 == 0:
    winner = "Brown"
else:
    winner = "Alice"

print(winner)

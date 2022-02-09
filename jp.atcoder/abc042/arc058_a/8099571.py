n, k = map(int, input().split())
money = n
dislike_digits = list(map(int, input().split()))

ok = False
found = False
while not ok:
    money_digits = [int(mon) for mon in str(money)]

    for digit in money_digits:
        for dis_digit in dislike_digits:
            if digit == dis_digit:
                found = True
                break
        if found:
            money += 1
            break

    if not found:
        ok = True

print(money)

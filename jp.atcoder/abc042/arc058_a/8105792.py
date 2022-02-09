price, size = map(int, input().split())
dislikes = list(map(int, input().split()))
likes = list(set(range(10)) - set(dislikes))

digits = [int(digit) for digit in str(price)]
digits.insert(0, 0) # 最後に0のままだったら除いて結合する、0じゃなければそのまま結合
found = False
ok = False

if size <= 5:
    for i in range(1, len(digits)+1):
        digit = digits[-i]
        while digit < 10:
            for dis in dislikes:
                if digit == dis:
                    found = True
                    break
            if found:
                digit += 1
                found = False
            else:
                digits[-i] = digit
                break
        if digit == 10:
            digits[-i-1] += 1
            digit = 0
            while digit < 10:
                for dis in dislikes:
                    if digit == dis:
                        found = True
                        break
                if found:
                    digit += 1
                    found = False
                else:
                    digits[-i] = digit
                    break
else:
    for i in range(1, len(digits)+1):
        digit = digits[-i]
        while digit < 10:
            for like in likes:
                if digit == like:
                    ok = True
                    break
            if not ok:
                digit += 1
            else:
                digits[-i] = digit
                break
        if digit == 10:
            digits[-i-1] += 1
            digit = 0
            while digit < 10:
                for like in likes:
                    if digit == like:
                        ok = True
                        break
                if not ok:
                    digit += 1
                else:
                    digits[-i] = digit
                    break


if digits[0] == 0:
    del digits[0]

ans = int(''.join([str(num) for num in digits]))
print(ans)

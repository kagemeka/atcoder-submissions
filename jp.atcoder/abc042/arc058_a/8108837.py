price, size = map(int, input().split())
dislikes = list(map(int, input().split()))
likes = list(set(range(10)) - set(dislikes))
digits = [int(digit) for digit in str(price)]
r_digits = list(reversed(digits))
res = []
for i in range(len(r_digits)):
    if r_digits[i] in likes:
        res.append(r_digits[i])
    elif max(likes) > r_digits[i]:
        res = [min(likes) for i in range(i)] + [min(x for x in likes if x > r_digits[i])]
    else:
        res = [min(likes) for i in range(i+1)]
        if i == len(r_digits)-1:
            res.append(min(x for x in likes if x > 0))

        else:
            r_digits[i+1] += 1

ans = "".join([str(num) for num in list(reversed(res))])
print(ans)

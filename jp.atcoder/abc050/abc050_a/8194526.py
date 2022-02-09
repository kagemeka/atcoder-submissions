A, op, B = input().split()
a, b = [int(x) for x in [A, B]]
if op == '+':
    ans = a + b
else:
    ans = a - b

print(ans)

N = int(input())
S = input()
x = 0
max_of_x = x

for char in S:
    if char == 'I':
        x += 1
        max_of_x = max(max_of_x, x)
    else:
        x -= 1

print(max_of_x)

colors = [color for color in input().split()]
colors.sort()

first = colors[0]

current = first
count = 1
for i in range(1, 3):
    if colors[i] != current:
        count += 1
        current = colors[i]

print(count)

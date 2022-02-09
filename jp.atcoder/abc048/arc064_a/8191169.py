n, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

count = 0
previous = 0

for i in a:
    if i + previous > x:
        excess = i + previous - x
        count += excess
        previous = x - previous
    else: # if not exceeding x.
        previous = i

print(count)

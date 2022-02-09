k, s = [int(x) for x in input().split()]
count = 0
for x in range(k+1):
    if x <= s:
        for y in range(k+1):
            if x + y <= s:
                z = s - (x + y)
                if  z <= k:
                    count += 1

print(count)

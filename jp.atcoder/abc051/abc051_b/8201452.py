K, S = [int(x) for x in input().split()]
count = 0
for x in range(K+1):
    # y + z = S - x
    if 0 <= S - x <= K:
        count += S - x + 1
        # yに選べるのは0から(y+z)までのy+z-0+1通りすなわちS-x+1
    elif K < S - x <= 2 * K:
        count += 2 * K - S + x + 1
        # K - ((S - x) - K) + 1
        # excess = (S-x)-K
    else:
        # S-x > 2Kだと、y+z > 2Kとなり、
        # こうなる組みは存在しない
        continue
print(count)

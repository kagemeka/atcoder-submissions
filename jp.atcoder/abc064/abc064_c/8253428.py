import sys
input = sys.stdin.readline

N = int(input())
rating = [int(r) for r in input().split()]
rating.sort()

color = ['gray', 'brown', 'green', 'cyan', 'blue', 'yellow', 'orange', 'red']
c_count = {c: 0 for c in color}

count_over = 0
for r in rating:
    if r < 400:    c_count[color[0]] += 1
    elif r < 800:  c_count[color[1]] += 1
    elif r < 1200: c_count[color[2]] += 1
    elif r < 1600: c_count[color[3]] += 1
    elif r < 2000: c_count[color[4]] += 1
    elif r < 2400: c_count[color[5]] += 1
    elif r < 2800: c_count[color[6]] += 1
    elif r < 3200: c_count[color[7]] += 1
    else:          count_over += 1

dif_c_count = 0
for v in c_count.values():
    if v != 0: dif_c_count += 1

mini, maxi = dif_c_count, dif_c_count + count_over
print(mini, maxi)

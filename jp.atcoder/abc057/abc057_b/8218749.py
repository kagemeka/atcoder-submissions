n, m = [int(x) for x in input().split()]
s_coords = [[int(_) for _ in input().split()] for i in range(n)]
c_coords = [[int(_) for _ in input().split()] for j in range(m)]

for i in s_coords:
    for j in range(1, m+1):
        man_dist = abs(c_coords[j - 1][0] - i[0]) + abs(c_coords[j - 1][1] - i[1])
        if j == 1:
            min_dist = man_dist
            destn_index = 1
        if min_dist > man_dist:
            min_dist = man_dist
            destn_index = j
    print(destn_index)

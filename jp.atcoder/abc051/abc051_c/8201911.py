sx, sy, tx, ty = [int(coodinate) for coodinate in input().split()]
d_x = tx - sx
d_y = ty - sy

route = []
route.append('U' * d_y + 'R' * d_x)
route.append('D' * d_y + 'L' * d_x)
route.append('L' + 'U' * (d_y + 1) +
    'R' * (d_x + 2))
route.append('D' * (d_y + 2) + 'L' * (d_x + 1)
    + 'U')

ans = ''.join(route)
print(ans)

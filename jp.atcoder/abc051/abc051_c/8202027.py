sx, sy, tx, ty = [int(coodinate) for coodinate in input().split()]
dx = tx - sx
dy = ty - sy

ans = ('L' + 'U' * (dy + 1) + 'R' * (dx + 1) +
    'D' * (dy + 1) + 'L' * dx + 'U' * dy +
    'R' * (dx + 1) + 'D' * (dy + 1) + 'L' * (dx + 1) +
    'U')

print(ans)

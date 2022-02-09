import sys
R, G, B = map(int, sys.stdin.readline().split())
# まずGを決め、それに対して、赤、青の置き方の最適解を求める。これをGについて全探索すれば良い。
def main():

    res = []
    for g in range(-G-50+1, 51):
        cnt_g = (1 + abs(g)) * abs(g) // 2 + (G + g) * (G - 1 + g) // 2
        if g <= -99:
            r = g - R + 100
            cnt_r = (abs(r) + abs(r + R - 1)) * R // 2
        else:
            can_right = g + 99
            r = min(-(R // 2), - (R - can_right - 1))
            cnt_r = (abs(r) + 1) * abs(r) // 2 + (R + r) * (R - 1 + r) // 2

        if G - 1 + g >= 99:
            b = G + g - 100
            cnt_b = (b + b + B - 1) * B // 2
        else:
            can_left = 99 - (G - 1 + g)
            b = max(B // 2, B - can_left - 1)# right
            cnt_b = (1 + b) * b // 2 + (B - b) * (B - b - 1) // 2
        res.append(cnt_g + cnt_r + cnt_b)

    print(min(res))

if __name__ == '__main__':
    main()

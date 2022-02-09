n, W = [int(x) for x in input().split()]
wv = [[int(x) for x in input().split()] for _ in range(n)] # weight, value

min_w = wv[0][0]

for i in range(n):
    wv[i].insert(0, wv[i][1] / wv[i][0])
wv.sort(reverse=1)  # sort in order that high value per unit weight.

sw = [0] * n   # camulative sum of weights
sw[0] = wv[0][1]
sv = [0] * n   # camulative sum of values
sv[0] = wv[0][2]
for i in range(n-1):
    sw[i+1] = sw[i] + wv[i+1][1]
    sv[i+1] = sv[i] + wv[i+1][2]

ans = 0
for i in range(n):
    if sw[i] < W:
        ans = sv[i] # continuous updating
        continue
    elif sw[i] == W:
        ans = sv[i]
        break
    else:
        if i > 0:
            d = W - sw[i-1]
            for j in range(d, min_w-1, -1):  # if d >= min_w
                for k in range(i+1, n):
                    if j == wv[k][1]:
                        ans += wv[k][2]
                        print(ans)
                        exit()
        else:
            for j in range(W, min_w-1, -1):
                for k in range(1, n):
                    if j == wv[k][1]:
                        ans += wv[k][2]
                        print(ans)
                        exit()


print(ans)

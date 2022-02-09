n, k = map(int, input().split())
dis = input().split()
m = n
while True:
    m = str(m)
    for d in dis:
        if d in m:
            break
    else:
        print(m)
        exit()

    m = int(m) + 1

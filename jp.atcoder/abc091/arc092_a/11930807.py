import sys
inf = float('inf')

n = int(sys.stdin.readline().rstrip())
res = zip(*[map(int, sys.stdin.read().split())] * 2)
res = sorted(zip(res, [1] * n + [0] * n))

def main():
    cnt = 0
    confirmed = [0] * n * 2
    for i in range(n * 2 - 2, -1, -1):
        if not res[i][1]: continue
        yr = res[i][0][1]
        yb = inf
        k = None
        for j in range(i + 1, n * 2):
            if res[j][1] or confirmed[j]: continue
            y = res[j][0][1]
            if y > yr and y < yb:
                yb = y; k = j
        if not k: continue
        confirmed[k] = 1
        cnt += 1
    print(cnt)

if __name__ ==  '__main__':
    main()

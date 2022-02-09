import sys

h, w, d = map(int, sys.stdin.readline().split())
a = [[int(x) for x in sys.stdin.readline().split()] for _ in range(h)]
q = int(sys.stdin.readline().rstrip())
lr = zip(*[map(int, sys.stdin.read().split())] * 2)

def main():
    place = [None] * (h * w + 1)
    for i in range(h):
        for j in range(w):
            place[a[i][j]] = (i, j)

    cost = [None] * (h * w + 1)
    for x in range(1, 1+d):
        cost[x] = 0
        i, j = place[x]
        while x + d <= h * w:
            nex = x + d
            nex_i, nex_j = place[nex]
            cost[nex] = cost[x] + abs(nex_i - i) + abs(nex_j - j)
            x = nex
            i, j = nex_i, nex_j

    for l, r in lr:
        yield cost[r] - cost[l]

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')

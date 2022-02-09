import sys

*I, = map(int, sys.stdin.read().split())
n, m = I[:2]
aby = I[2:2+m*3]
a = aby[::3]
b = aby[1::3]
y = aby[2::3]
yab = list(zip(y, a, b))
q = I[2+m*3]
vw = I[(m+1)*3:]
wv = list(zip(vw[1::2], vw[::2]))

yab.sort(reverse=True)
jwv = sorted(list(enumerate(wv)), reverse=True, key=lambda x: x[1])


parent = [None] * (n + 1)
num_of_memb = [1] * (n + 1)

def union(v, u):
    while parent[v]:
        v = parent[v]
    root_v = v
    while parent[u]:
        u = parent[u]
    root_u = u
    if root_u != root_v:
        parent[root_v] = root_u
        num_of_memb[u] += num_of_memb[v]

def find(v):
    while parent[v]:
        v = parent[v]
    root = v
    return root

def main():
    i = 0
    res = [0] * q
    for j, wv in jwv:
        w, v = wv
        cnt = 0
        for y, a, b in yab[i:]:
            if y <= w:
                break
            union(a, b)
            cnt += 1
        i += cnt
        res[j] = num_of_memb[find(v)]
    return res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')

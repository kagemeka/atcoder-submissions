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


root = list(range(n+1))
size = [1] * (n + 1)
height = [1] * (n + 1)

def find_root(v):
    x = root[v]
    if x == v:
        return v
    root[v] = find_root(x)
    return root[v]

def unite(v, u):
    rv = find_root(v)
    ru = find_root(u)
    if rv != ru:
        hv = height[rv]
        hu = height[ru]
        if hv >= hu:
            root[ru] = rv
            size[rv] += size[ru]
            height[rv] = max(hv, hu+1)
        else:
            root[rv] = ru
            size[ru] += size[rv]

def main():
    i = 0
    res = [0] * q
    for j, wv in jwv:
        w, v = wv
        cnt = 0
        for y, a, b in yab[i:]:
            if y <= w:
                break
            unite(a, b)
            cnt += 1
        i += cnt
        res[j] = size[find_root(v)]
    return res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')

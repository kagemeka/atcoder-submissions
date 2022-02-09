import typing
import bisect

def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if n == 1:
        if k & 1:
            print(a[0])
        else:
            print()
        return
    m = 1 << 18
    nxt = [-1] * m
    for i in range(n):
        x = a[i]
        if nxt[x] != -1: continue
        nxt[x] = i
    b = [-1] * n
    for i in range(n - 1, -1, -1):
        b[i] = (nxt[a[i]] + 1) % n
        nxt[a[i]] = i
    order = [0]
    while True:
        order.append(b[order[-1]])
        if order[-1] == 0: break


    s = [0] * len(order)
    for i in range(len(order) - 1):
        d = order[i + 1] - order[i]
        if d <= 1:
            d += n
        s[i + 1] = s[i] + d

    assert s[-1] % n == 0
    cycle = s[-1] // n
    k %= cycle
    if k == 0:
        print()
        return

    i = -1
    while s[i + 1] < k * n - 1: i += 1
    a = a[s[i] % n:]
    added = set()
    st = []
    for x in a:
        if not x in added:
            added.add(x)
            st.append(x)
            continue
        while True:
            y = st.pop()
            added.remove(y)
            if y == x: break
    print(*st)

main()

import typing


def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    pos = []
    neg = []
    for x in a:
        if x > 0: pos.append(x)
        if x < 0: neg.append(x)


    positive_possible = False
    if k & 1 and len(pos) >= 1 and len(pos) + len(neg) // 2 * 2 >= k:
        positive_possible = True
    elif ~k & 1 and len(pos) // 2 * 2 + len(neg) // 2 * 2 >= k:
        positive_possible = True

    MOD = 10 ** 9 + 7
    if not positive_possible:
        if 0 in a:
            print(0)
            return
        p = 1
        for x in sorted(a, key=lambda x: abs(x))[:k]:
            p *= x
            p %= MOD
        print(p)
        return

    pos.sort(reverse=True)
    neg.sort()
    cand = []
    if k & 1:
        p = pos[0]
        pos = pos[1:]
        k -= 1
    else:
        p = 1
    for i in range(len(pos) // 2):
        cand.append(pos[2 * i] * pos[2 * i + 1])
    for i in range(len(neg) // 2):
        cand.append(neg[2 * i] * neg[2 * i + 1])
    assert all(x > 0 for x in cand)
    cand.sort(reverse=True)
    for x in cand[:k // 2]:
        p *= x
        p %= MOD
    print(p)



main()

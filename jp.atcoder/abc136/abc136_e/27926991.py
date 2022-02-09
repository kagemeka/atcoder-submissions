import typing

def find_divisors(n: int) -> typing.List[int]:
    divs = []
    i = 1
    while i * i <= n:
        if n % i != 0:
            i += 1
            continue
        divs.append(i)
        if n // i != i: divs.append(n // i)
        i += 1
    return sorted(divs)


def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    mx = 1
    for d in find_divisors(s)[1:]:
        neg = []
        pos = []
        for x in a:
            r = x % d
            if r <= d - r:
                neg.append(r)
            else:
                pos.append(d - r)
        pos.sort()
        neg.sort()
        sn = sum(neg)
        sp = sum(pos)
        cn = len(neg)
        cp = len(pos)
        assert (sp - sn) % d == 0
        if (sp - sn) % d != 0: continue
        while sp - sn != 0:
            if sp - sn > 0:
                if pos:
                    x = pos.pop()
                    sp -= x
                    sn += d - x
                else:
                    sn = sp
            else:
                if neg:
                    x = neg.pop()
                    sn -= x
                    sp += d - x
                else:
                    sp = sn
        if max(sp, sn) <= k:
            mx = max(mx, d)

    print(mx)


main()

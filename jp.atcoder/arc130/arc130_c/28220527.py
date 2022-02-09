import typing
import collections

def main() -> typing.NoReturn:
    a = list(map(int, input()))
    b = list(map(int, input()))
    swapped = False
    if len(a) < len(b):
        a, b = b, a
        swapped = True

    ca = collections.Counter(a)
    cb = collections.Counter(b)

    # for a, as small as possible

    res_a = []
    res_b = []
    tot = 0
    flg = False
    for s in range(10, 19):
        for i in range(8, -1, -1):
            i = (i - 1) % 9 + 1
            j = s - i
            assert j >= 1
            if 10 <= j: continue
            if ca[i] == 0 or cb[j] == 0: continue
            ca[i] -= 1
            cb[j] -= 1
            flg = True
            res_a.append(i)
            res_b.append(j)
            tot += s % 10
            break
        if flg: break

    if not flg:
        # there is no pair such that i + j >= 10
        # so no digit cannot be carried up.
        if swapped: a, b = b, a
        print(''.join(map(str, a)))
        print(''.join(map(str, b)))
        return


    for i in range(1, 10):
        for s in range(9, 19):
            j = s - i
            if 10 <= j: continue
            while ca[i] >= 1 and cb[j] >= 1:
                ca[i] -= 1
                cb[j] -= 1
                res_a.append(i)
                res_b.append(j)
                tot += (s + 1) % 10

    if ca[9] >= 1:
        res_a += [9] * ca[9]
        ca[9] = 0
        for i in range(1, 10):
            res_a += [i] * ca[i]
            tot += ca[i] * i
            ca[i] = 0
            assert cb[i] == 0
    else:
        for i in range(1, 10):
            res_b += [i] * cb[i]
            res_a += [i] * ca[i]
            tot += i * (ca[i] + cb[i])
            ca[i] = cb[i] = 0
    tot += 1
    # for i in range(1, 10):
    #     res_b += [i] * cb[i]
    #     res_a += [i] * ca[i]
    #     tot += i * (ca[i] + cb[i])
    #     cb[i] = ca[i] = 0
    # tot += 1
    print(tot)
    a = ''.join(map(str, res_a))[::-1]
    b = ''.join(map(str, res_b))[::-1]
    if swapped:
        a, b = b, a
    print(a)
    print(b)


main()

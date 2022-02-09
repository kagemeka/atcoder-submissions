import typing


def main() -> typing.NoReturn:
    k = int(input())

    que = [[i] for i in range(1, 10)]
    if k <= 9:
        print(que[k - 1][0])
        return


    k -= 9
    for a in que:
        x = a[-1]
        for y in range(max(0, x - 1), min(9, x + 1) + 1):
            b = a.copy()
            b.append(y)
            que.append(b)
            k -= 1
            if k == 0: break
        if k == 0: break
    print(''.join(map(str, que[-1])))

main()

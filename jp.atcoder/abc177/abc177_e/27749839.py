import typing

def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    k = 1 << 20
    f = [0] * k
    for x in a:
        f[x] += 1
    for i in range(2, k):
        for j in range(2 * i, k, i):
            f[i] += f[j]
    if max(f[2:]) <= 1:
        print('pairwise coprime')
    elif max(f) < n:
        print('setwise coprime')
    else:
        print('not coprime')


main()

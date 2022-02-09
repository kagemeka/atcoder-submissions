import typing



def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input()))
    # odd, even
    a = [x - 1 for x in a]
    k = 1 << 20
    cnt2 = [0] * k
    cnt2[2] = 1
    for i in range(2, k):
        if i * 2 >= k: break
        cnt2[i * 2] = cnt2[i] + 1

    for i in range(k - 1):
        cnt2[i + 1] += cnt2[i]

    def is_odd(a: typing.List[int]) -> bool:
        n = len(a)
        bl = 0
        for i in range(n):
            # n - 1 choose i
            # (n - 1)! / i! * (n - 1 - i)!
            bl ^= (a[i] & 1) & cnt2[n - 1] == cnt2[i] + cnt2[n - 1 - i]
        return bl

    if is_odd(a):
        print(1)
        return
    if 1 in a:
        print(0)
        return
    a = [x // 2 for x in a]
    if is_odd(a):
        print(2)
    else:
        print(0)

main()

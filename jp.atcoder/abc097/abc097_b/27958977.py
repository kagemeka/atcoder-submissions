import typing


def main() -> typing.NoReturn:
    n = int(input())
    ok = [False] * (n + 1)
    ok[1] = True
    for i in range(2, n):
        if i * i > n: break
        j = i * i
        while j <= n:
            ok[j] = True
            j *= i
    mx = 1
    for i in range(n + 1):
        if not ok[i]: continue
        mx = max(mx, i)
    print(mx)


main()

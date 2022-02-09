import typing

def main() -> typing.NoReturn:
    n, k = map(int, input().split())

    c = 0
    for b in range(1, n + 1):
        if b <= k: continue
        q, r = divmod(n, b)
        c += q * (b - k) - (k == 0) + max(0, r - k + 1)
    print(c)

main()

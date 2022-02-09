import typing


def main() -> typing.NoReturn:
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0] + k)
    ans = k - max(a[i + 1] - a[i] for i in range(n))
    print(ans)

main()

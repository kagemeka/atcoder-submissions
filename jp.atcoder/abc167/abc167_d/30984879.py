import typing


def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= 1

    # doubling
    identity = list(range(n))

    def pow(a: typing.List[int], n: int) -> typing.List[int]:
        if n == 0:
            return identity
        b = pow(a, n >> 1)
        b = [b[i] for i in b]
        if n & 1:
            b = [b[i] for i in a]
        return b

    b = pow(a, k)
    print(b[0] + 1)


if __name__ == "__main__":
    main()

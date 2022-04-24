def solve() -> int:
    n, a, b, x, y, z = map(int, input().split())
    y = min(y, a * x)
    z = min(z, b * x)
    if y * b > z * a:
        a, b = b, a
        y, z = z, y

    mn_cost = 1 << 60
    if n // a <= a - 1:
        for i in range(n // a + 1):
            j, k = divmod(n - i * a, b)
            mn_cost = min(mn_cost, i * y + j * z + k * x)
    else:
        for j in range(a):
            i, k = divmod(n - j * b, a)
            mn_cost = min(mn_cost, i * y + j * z + k * x)
    return mn_cost


def main() -> None:
    t = int(input())
    res = []
    for _ in range(t):
        res.append(solve())
    print(*res, sep="\n")


if __name__ == "__main__":
    main()

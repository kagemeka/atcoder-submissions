import typing


def main() -> typing.NoReturn:
    n, m =  map(int, input().split())
    a = list(map(int, input().split()))
    prev = [-1] * n
    cand = []
    for i in range(n):
        if i - prev[a[i]] > m:
            cand.append(a[i])
            continue
        prev[a[i]] = i

    for x in range(n):
        if n - prev[x] > m:
            cand.append(x)

    print(min(cand) if cand else n)

main()

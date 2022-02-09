import typing


def main() -> typing.NoReturn:
    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    a, b = zip(*ab)
    a_idx = sorted(range(n), key=lambda i: a[i])
    b_idx = sorted(range(n), key=lambda i: b[i])
    if a_idx[0] != b_idx[0]:
        print(max(a[a_idx[0]], b[b_idx[0]]))
        return
    if a[a_idx[1]] > b[b_idx[1]]:
        a, b = b, a
        a_idx, b_idx = b_idx, a_idx
    print(min(a[a_idx[0]] + b[b_idx[0]], max(a[a_idx[1]], b[b_idx[0]])))

main()

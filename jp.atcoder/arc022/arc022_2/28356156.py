import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    # shakutori algorithm.

    mx = 1
    cnt = [0] * (1 << 17)
    l = 0
    for i in range(n):
        cnt[a[i]] += 1
        while cnt[a[i]] >= 2:
            cnt[a[l]] -= 1
            l += 1
        mx = max(mx, i + 1 - l)

    print(mx)

main()

# / mypy: ignore-errors
import typing


def main() -> None:
    n, q, x = map(int, input().split())
    w = list(map(int, input().split()))
    queries = [int(input()) for _ in range(q)]

    # cumsum
    s = sum(w)
    c = x // s
    x %= s
    w2 = w + w
    next = [-1] * n
    r = 0
    tmp = 0
    cnt = [0] * n
    # if x == 0:
    #     for i in range(n):
    #         next[i] = i
    #         cnt[i] = c
    # else:
    for i in range(n):
        while tmp < x:
            tmp += w2[r]
            r += 1
        assert i <= r <= i + n
        cnt[i] = r - i + c
        next[i] = r % n
        tmp -= w2[i]
    i = 0
    j = 0
    indices = [-1] * n
    indices[i] = j
    loop = [i]
    while True:
        j += 1
        i = next[i]
        if indices[i] == -1:
            indices[i] = j
            loop.append(i)
            continue
        start = indices[i]
        loop2 = loop[indices[i] :]
        break
    size = len(loop2)
    for k in queries:
        k -= 1
        if k < start:
            j = loop[k]
        else:
            k = (k - start) % size
            j = loop2[k]
        print(cnt[j])


main()

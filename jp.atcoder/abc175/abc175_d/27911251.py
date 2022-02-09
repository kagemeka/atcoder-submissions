import typing


def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    p = list(map(lambda x: int(x) - 1, input().split()))
    c = list(map(int, input().split()))
    inf = 1 << 60
    mx = -inf
    for i in range(n):
        # visiting order
        # loop size
        # first visiting score
        # loop score
        score = [-inf] * n
        score[i] = 0
        order = [-1] * n
        order[i] = 0
        for _ in range(n):
            x = p[i]
            if score[x] != -inf:
                loop_size = order[i] + 1 - order[x]
                loop_score = score[i] + c[x] - score[x]
                break
            order[x] = order[i] + 1
            score[x] = score[i] + c[x]
            i = x
        else:
            raise
        for i in range(n):
            if order[i] <= 0: continue
            if order[i] > k: continue
            s = score[i]
            if loop_score > 0:
                s += (k - order[i]) // loop_size * loop_score
            mx = max(mx, s)
    print(mx)


main()

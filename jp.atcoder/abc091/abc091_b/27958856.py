import typing
import collections

def main() -> typing.NoReturn:
    n = int(input())
    s = [input() for _ in range(n)]
    m = int(input())
    t = [input() for _ in range(m)]
    cnt = collections.Counter(s)
    cnt_t = collections.Counter(t)
    for k, v in cnt_t.items():
        cnt[k] -= v
    print(max(0, max(cnt.values())))

main()

import typing
import collections

def main() -> typing.NoReturn:
    n = int(input())
    s = input()


    def count_up(s: str) -> typing.Dict[typing.Tuple[str, str], int]:
        assert len(s) == n
        cnt = collections.defaultdict(int)
        for t in range(1 << n):
            r = ''
            b = ''
            for i in range(n):
                if t >> i & 1:
                    r += s[i]
                else:
                    b += s[i]
            cnt[(r, b)] += 1
        return cnt


    cnt0 = count_up(s[:n])
    cnt1 = count_up(s[:n - 1:-1])

    cnt = 0
    for (r, b), c in cnt0.items():
        cnt += c * cnt1[(b, r)]
    print(cnt)

main()

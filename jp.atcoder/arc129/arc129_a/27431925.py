import typing





def main() -> typing.NoReturn:
    n, l, r = map(int, input().split())

    def f(k: int) -> int:
        cnt = 0
        for i in range(63):
            if 1 << i > k: break
            if ~n >> i & 1: continue
            if i == k.bit_length() - 1:
                cnt += (k & ((1 << i) - 1)) + 1
            else:
                cnt += (1 << i)
        return cnt

    print(f(r) - f(l - 1))


main()

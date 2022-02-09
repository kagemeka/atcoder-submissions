import typing




def main() -> typing.NoReturn:
    n = int(input())

    def query(u: int, v: int) -> int:
        q = f'? {u + 1} {v + 1}'
        print(q, flush=True)
        return int(input())


    def get_farest(u: int) -> typing.Tuple[int, int]:
        mx = 0
        v = -1
        for i in range(n):
            if i == u: continue
            d = query(u, i)
            if d <= mx: continue
            mx = d
            v = i
        return v, mx


    u, _ = get_farest(0)
    _, d = get_farest(u)
    print(f'! {d}')

main()

import typing

def main() -> typing.NoReturn:
    n = int(input())
    a = set()
    b = set()
    for _ in range(n):
        s = input()
        if s[0] == '!': b.add(s[1:])
        else: a.add(s)
    for s in a:
        if not s in b: continue
        print(s)
        return

    print('satisfiable')

main()

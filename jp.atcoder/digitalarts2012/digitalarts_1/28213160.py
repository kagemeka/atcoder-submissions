import typing



def match(s: str, t: str) -> bool:
    n = len(s)
    if len(t) != n: return False
    for i in range(n):
        if t[i] == '*': continue
        if t[i] != s[i]: return False
    return True


def main() -> typing.NoReturn:
    a = input().split()
    n = int(input())
    b = [input() for _ in range(n)]
    for i, s in enumerate(a):
        for t in b:
            if not match(s, t): continue
            a[i] = '*' * len(s)
            break
    print(*a)

main()

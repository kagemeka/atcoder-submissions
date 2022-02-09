import typing

def main() -> typing.NoReturn:
    s = input()
    t = s.lower()
    ok = True

    ok &= sum(s[i] != t[i] for i in range(len(s))) == 2
    ok &= s[0] == 'A'
    ok &= 'C' in s[2:-1]
    print('AC' if ok else 'WA')

main()

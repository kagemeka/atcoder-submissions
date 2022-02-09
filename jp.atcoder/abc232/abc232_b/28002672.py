import typing
import string

def main() -> typing.NoReturn:
    s = input()
    t = input()
    s = list(s)
    t = list(t)
    alp = string.ascii_lowercase
    idx = dict(zip(alp, range(26)))

    for k in range(25):
        w = [alp[(idx[x] + k) % 26] for x in s]
        if w == t:
            print('Yes')
            return
    print('No')




main()

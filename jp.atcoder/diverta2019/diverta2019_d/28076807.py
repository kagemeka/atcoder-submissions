import typing



def main() -> typing.NoReturn:
    n = int(input())

    divs = []
    for i in range(1, n + 1):
        if i * i > n: break
        if n % i: continue
        divs.append(i)
        if n // i != i: divs.append(n // i)
    divs.sort()


    s = 0
    for i in divs:
        j = n // i
        s += (j < i - 1) * (i - 1)

    print(s)

main()
